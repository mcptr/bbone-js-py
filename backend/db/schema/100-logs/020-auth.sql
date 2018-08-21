CREATE TABLE logs.auth (
    id bigserial primary key,
    user_id integer default null references auth.users(id) on update cascade on delete set null,
    user_ident character varying(255) DEFAULT NULL::character varying,
    success boolean NOT NULL,
    origin character varying(32) NOT NULL,
    client_agent character varying(255) DEFAULT NULL::character varying
);
