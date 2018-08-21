CREATE TABLE stats.downloads (
    id bigserial primary key,
    file_id integer not null references storage.media(id) on update cascade on delete cascade,
    origin character varying(32) DEFAULT NULL::character varying
);

