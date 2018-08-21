CREATE TABLE logs.search_keywords (
    id bigserial primary key,
    ident character varying(64) NOT NULL,
    ctime timestamp not null default now()
);

create index search_keywords_ident_idx on logs.search_keywords(ident);
