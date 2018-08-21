CREATE TABLE auth.users (
    id serial primary key,
    ident character varying(255) NOT NULL UNIQUE,
    username character varying(255) NOT NULL UNIQUE,
    password character varying(64) NOT NULL,
    active boolean DEFAULT true NOT NULL,
    ctime timestamp without time zone DEFAULT now() NOT NULL,
    mtime timestamp without time zone DEFAULT now() NOT NULL,
    confirmed boolean DEFAULT FALSE NOT NULL,
    last_success timestamp default NULL,
    last_failure timestamp default NULL,
    failures integer default 0,
    address text DEFAULT NULL,
    city character varying(128) DEFAULT NULL::character varying,
    country character varying(128) DEFAULT NULL::character varying,
    phone character varying(64) DEFAULT NULL::character varying,
    gender types.gender_t DEFAULT NULL,
    date_of_birth date DEFAULT NULL,
    social_uid varchar(64) DEFAULT NULL,
    social_provider varchar(32) DEFAULT NULL

    CONSTRAINT users_username_check CHECK (((length((username)::text) >= 0) AND (length((username)::text) <= 255))),
    CONSTRAINT users_ident_check CHECK (((length((ident)::text) >= 6) AND (length((ident)::text) <= 255))),
    CONSTRAINT users_password_check CHECK (((length((password)::text) >= 6) AND (length((password)::text) <= 64)))
);

CREATE INDEX users_city_idx ON auth.users USING btree (city);
CREATE INDEX users_country_idx ON auth.users USING btree (country);
