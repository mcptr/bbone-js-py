CREATE TABLE core.config (
    ident character varying(128) primary key,
    option_type types.config_option_t NOT NULL,
    bool_value boolean,
    string_value text,
    int_value integer,
    double_value numeric(10,3) DEFAULT NULL::numeric,
    data text
);
