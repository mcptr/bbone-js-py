CREATE OR REPLACE VIEW views.users AS
       SELECT u.id,
	      u.ident,
	      u.ctime,
	      u.confirmed,
	      u.active,
	      u.username,
	      u.city,
	      u.country
	FROM auth.users u
	ORDER BY u.username DESC;

CREATE OR REPLACE VIEW views.active_users AS
       SELECT u.id,
	      u.ident,
	      u.ctime,
	      u.confirmed,
	      u.active,
	      u.username,
	      u.city,
	      u.country
	FROM auth.users u
	WHERE u.active = true
	ORDER BY u.username DESC;


CREATE OR REPLACE VIEW views.authenticated_users AS
       SELECT s.id AS session_id,
	      u.id as user_id,
	      u.ident as user_ident,
	      u.username,
	      extract('epoch' from u.ctime) as user_ctime,
	      extract('epoch' from u.mtime) as user_mtime,
	      extract('epoch' from u.last_success) as last_success,
	      extract('epoch' from u.last_failure) as last_failure,
	      u.failures,
	      extract('epoch' from s.ctime) as session_ctime,
	      extract('epoch' from s.mtime) as session_mtime,
	      u.confirmed,
	      array_agg(g.ident) as user_groups,
	      u.city,
	      u.country,
	      s.data as session_data
	FROM auth.users u
	   JOIN auth.sessions s ON s.user_id = u.id
	   LEFT JOIN auth.user_group_map ugm on ugm.user_id = u.id
	   LEFT JOIN auth.groups g on g.id = ugm.group_id
	   WHERE u.active = TRUE
	   AND extract('epoch' from (now() - s.mtime)) < (
		SELECT int_value FROM core.config
		       WHERE ident = 'session_max_age'
	   )
	   GROUP BY u.id, s.id, u.username, u.city, u.country;
