CREATE TABLE geo.currencies (
    id serial primary key,
    iso_code character(3) NOT NULL unique,
    ident character varying(64) DEFAULT NULL::character varying
);

CREATE TRIGGER trg_uc_ident BEFORE INSERT OR UPDATE ON geo.currencies
       FOR EACH ROW EXECUTE PROCEDURE generic.trg_uc_ident();
