CREATE TABLE auth.groups (
    id serial primary key,
    ident character varying(255) NOT NULL UNIQUE,
    active boolean DEFAULT TRUE NOT NULL,
    ctime timestamp without time zone DEFAULT now() NOT NULL
);
