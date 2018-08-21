CREATE TABLE storage.post_categories (
    id serial primary key,
    ident varchar(64) not null,
    parent_id integer default null references storage.post_categories(id) on update cascade on delete cascade,
    active boolean not null default true
);

CREATE UNIQUE INDEX post_category_uidx on storage.post_categories(ident, parent_id); 

CREATE TRIGGER trg_lc_ident BEFORE INSERT OR UPDATE ON storage.post_categories
        FOR EACH ROW EXECUTE PROCEDURE generic.trg_lc_ident();
