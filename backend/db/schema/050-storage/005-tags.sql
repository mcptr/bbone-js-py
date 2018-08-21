CREATE TABLE storage.tags (
    id serial primary key,
    ident character varying(128) NOT NULL UNIQUE,
    active boolean DEFAULT true NOT NULL,
    ctime timestamp not null default current_timestamp
);

CREATE TRIGGER trg_lc_ident BEFORE INSERT OR UPDATE ON storage.tags
   FOR EACH ROW EXECUTE PROCEDURE generic.trg_lc_ident();
