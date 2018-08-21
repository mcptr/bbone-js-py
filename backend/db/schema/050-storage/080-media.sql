CREATE TABLE storage.media (
    id bigserial primary key,
    original_name character varying(255) not null,
    title character varying(255) DEFAULT NULL::character varying,
    active boolean DEFAULT true NOT NULL,
    access_modifier types.access_modifier_t DEFAULT 'PUBLIC'::types.access_modifier_t,
    ctime timestamp without time zone DEFAULT now() NOT NULL,
    file_size bigint NOT NULL,
    mime_type character varying(64) DEFAULT NULL::character varying,
    media_root varchar(255) not null,
    path varchar(255) not null,
    node varchar(128) default null
);
