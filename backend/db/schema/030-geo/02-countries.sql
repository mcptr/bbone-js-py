CREATE TABLE geo.countries (
    id serial primary key,
    ident character varying(128) NOT NULL unique,
    code character(3) DEFAULT NULL::bpchar,
    currency_id integer default null references geo.currencies(id) on update cascade on delete restrict,
    localized_name character varying(64) DEFAULT NULL::character varying,
    latitude numeric(8,4) DEFAULT NULL::numeric,
    longitude numeric(8,4) DEFAULT NULL::numeric,
    radius integer,
    CONSTRAINT countries_ident_check CHECK (length((ident)::text) > 0)
);


CREATE TRIGGER trg_initcap_ident BEFORE INSERT OR UPDATE ON geo.countries
   FOR EACH ROW EXECUTE PROCEDURE generic.trg_initcap_ident();

CREATE TRIGGER trg_uc_code BEFORE INSERT OR UPDATE ON geo.countries
   FOR EACH ROW EXECUTE PROCEDURE generic.trg_uc_code();
