CREATE TABLE logs.search_queries (
    id bigserial primary key,
    user_id integer default null references auth.users(id) on update cascade on delete no action,
    content text NOT NULL,
    ctime timestamp without time zone DEFAULT now() NOT NULL
);
