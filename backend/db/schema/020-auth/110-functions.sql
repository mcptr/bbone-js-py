CREATE OR REPLACE FUNCTION auth.authenticate(
       user_ident varchar,
       user_password varchar,
       client_origin varchar,
       client_agent varchar default NULL,
       session_id varchar default NULL
       )
       RETURNS VARCHAR
AS $$
   DECLARE _id integer = 0;
   DECLARE _success boolean = FALSE;
   DECLARE _session_id VARCHAR = '';

   BEGIN
      SELECT id INTO _id
      FROM auth.users
           WHERE (LOWER(ident) = LOWER(user_ident) OR LOWER(username) = LOWER(user_ident))
           AND crypt(user_password, password) = password
           AND failures < (SELECT int_value FROM core.config WHERE ident = 'max_login_failures');

      IF FOUND THEN
         UPDATE auth.users
             SET last_success = now()--, failures = 0
         WHERE id = _id;

         _success = TRUE;
      ELSE 
         UPDATE auth.users
             SET last_failure = now(), failures = (failures + 1)
         WHERE (LOWER(ident) = LOWER(user_ident) OR LOWER(username) = LOWER(user_ident));

         _success = FALSE;
      END IF;

      EXECUTE logs.log_auth(user_ident, _success, client_origin, client_agent, _id);

      IF _success THEN
         IF LENGTH(session_id) > 0 THEN
             UPDATE auth.sessions SET user_id = _id WHERE id = session_id
                 RETURNING id INTO _session_id;
             IF NOT FOUND THEN
                 _session_id = '';
             END IF;
         ELSE
             INSERT INTO auth.sessions (id, user_id)
                 VALUES(uuid_generate_v4(), _id) RETURNING id INTO _session_id;
         END IF;
      END IF;

      RETURN _session_id;
   END;
$$
language 'plpgsql';


CREATE OR REPLACE FUNCTION auth.touch_session(
       session_id varchar,
       client_agent_ varchar default NULL,
       client_origin_ varchar default NULL
       ) RETURNS BOOLEAN
AS $$
   DECLARE _session_id varchar;

   BEGIN
     SELECT s.id INTO _session_id FROM auth.sessions s
        WHERE s.id = session_id
        AND extract('epoch' from (now() - s.mtime)) < (
            SELECT int_value FROM core.config WHERE LOWER(ident) = 'session_max_age'
        )
        AND client_origin = client_origin_
        AND client_agent = client_agent_;

     IF FOUND THEN
        UPDATE auth.sessions SET mtime = now() WHERE id = _session_id;
        RETURN TRUE;
     ELSE
        RETURN FALSE; 
     END IF;
   END;
$$
LANGUAGE 'plpgsql';


CREATE OR REPLACE FUNCTION auth.read_session(session_id varchar) RETURNS setof RECORD
AS $$
   BEGIN
        PERFORM auth.touch_session(session_id);
        RETURN QUERY
            SELECT s.id, s.ctime, s.mtime, s.user_id, s.permanent, s.data
            FROM auth.sessions s
            WHERE s.id = session_id AND
            extract('epoch' from (now() - s.mtime)) < (
                SELECT int_value FROM core.config WHERE ident = 'session_max_age'
            );
   END;
$$
LANGUAGE 'plpgsql'
RETURNS NULL ON NULL INPUT;


CREATE OR REPLACE FUNCTION auth.verify_confirmation(
       user_id_ INTEGER,
       action_type_ VARCHAR,
       confirmation_key_ VARCHAR
       ) RETURNS BOOLEAN
AS $$
   BEGIN
      UPDATE auth.user_confirmations
             SET confirmed_on = NOW()
             WHERE user_id = user_id_
                   AND confirmation_key = confirmation_key_
                   AND UPPER(action_type) = UPPER(action_type_)
                   AND extract('epoch' from (now() - ctime)) < max_age
                   AND confirmed_on IS NULL;

     IF FOUND THEN
        RETURN TRUE;
     ELSE
        RETURN FALSE;
     END IF;

   END
$$
LANGUAGE 'plpgsql'
RETURNS NULL ON NULL INPUT;


CREATE OR REPLACE FUNCTION auth.confirm_user_registration(
       user_id_ INTEGER,
       action_type_ VARCHAR,
       confirmation_key_ VARCHAR
       ) RETURNS BOOLEAN
AS $$
   DECLARE confirmation_success BOOLEAN;
   DECLARE success BOOLEAN = FALSE;
   BEGIN
   	SELECT verify_confirmation INTO confirmation_success
	       FROM auth.verify_confirmation(user_id_, action_type_, confirmation_key_);
	IF confirmation_success THEN
		UPDATE auth.users SET confirmed = TRUE WHERE id = user_id_;
		IF FOUND THEN
		    success = TRUE;
		ELSE
		    success = FALSE;
		END IF;
	END IF;

	RETURN success;
   END
$$
LANGUAGE 'plpgsql'
RETURNS NULL ON NULL INPUT;
