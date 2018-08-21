CREATE TABLE logs.search_locations (
    id bigserial primary key,
    ident character varying(64) NOT NULL,
    ctime timestamp not null default now()
);

create index search_locations_ident_idx on logs.search_locations(ident);
