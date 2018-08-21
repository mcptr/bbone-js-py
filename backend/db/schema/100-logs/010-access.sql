CREATE TABLE logs.access (
    id bigserial primary key,
    tstamp timestamp without time zone DEFAULT now() NOT NULL,
    status types.access_status_t NOT NULL,
    origin character varying(32) NOT NULL,
    client_agent character varying(255) DEFAULT NULL::character varying,
    resource character varying(1024) NOT NULL,
    user_id integer default null references auth.users(id) on update cascade on delete no action
);

CREATE INDEX access_origin_idx ON logs.access USING btree (origin);
CREATE INDEX access_resource_idx ON logs.access USING btree (resource);
CREATE INDEX access_tstamp_idx ON logs.access USING btree (tstamp);
