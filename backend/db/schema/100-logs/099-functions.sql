CREATE OR REPLACE FUNCTION logs.log_auth(
       user_ident varchar,
       success boolean,
       client_origin varchar,
       client_agent varchar default NULL,
       user_id integer default NULL
      )
      RETURNS VOID
AS $$
   BEGIN
	INSERT INTO logs.auth(user_id, user_ident, success, origin, client_agent)
	    VALUES(user_id, user_ident, success, client_origin, client_agent);
   END;
$$
LANGUAGE plpgsql;


