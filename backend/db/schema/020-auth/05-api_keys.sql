CREATE TABLE auth.api_keys (
    api_key character varying(64) NOT NULL primary key,
    key_type types.api_key_t NOT NULL,
    -- these are used separately
    user_id integer default null references auth.users(id) on update cascade on delete cascade,
    group_id integer default null references auth.groups(id) on update cascade on delete cascade,
    active boolean DEFAULT true NOT NULL,
    ctime timestamp without time zone DEFAULT now() NOT NULL
);
