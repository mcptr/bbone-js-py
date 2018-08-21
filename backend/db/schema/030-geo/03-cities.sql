CREATE TABLE geo.cities (
    id serial NOT NULL primary key,
    ident character varying(128) NOT NULL,
    code character varying(6) DEFAULT NULL::character varying,
    country_id integer not null references geo.countries(id) on update cascade on delete cascade,
    localized_name character varying(64) DEFAULT NULL::character varying,
    latitude numeric(8,4) DEFAULT NULL::numeric,
    longitude numeric(8,4) DEFAULT NULL::numeric,
    radius integer,
    CONSTRAINT cities_ident_check CHECK (length((ident)::text) > 0)
);

CREATE UNIQUE INDEX ON geo.cities(ident, country_id);

CREATE TRIGGER trg_initcap_ident BEFORE INSERT OR UPDATE ON geo.cities
   FOR EACH ROW EXECUTE PROCEDURE generic.trg_initcap_ident();

CREATE TRIGGER trg_uc_code BEFORE INSERT OR UPDATE ON geo.cities
   FOR EACH ROW EXECUTE PROCEDURE generic.trg_uc_code();
