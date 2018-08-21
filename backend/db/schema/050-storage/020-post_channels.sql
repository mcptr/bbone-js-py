CREATE TABLE storage.post_channels (
    id serial primary key,
    ident character varying(128) NOT NULL unique,
    parent_id integer default null references storage.post_categories(id) on update cascade on delete cascade,
    active boolean DEFAULT true NOT NULL
);
