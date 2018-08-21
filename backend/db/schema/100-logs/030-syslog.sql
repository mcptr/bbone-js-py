CREATE TABLE logs.syslog (
    id serial,
    level types.syslog_level_t DEFAULT 'INFO'::types.syslog_level_t NOT NULL,
    tstamp timestamp without time zone DEFAULT now() NOT NULL,
    message text NOT NULL,
    data text
);

CREATE INDEX syslog_level_idx ON logs.syslog USING btree (level);
