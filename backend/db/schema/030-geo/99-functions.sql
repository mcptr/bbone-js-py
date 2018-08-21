CREATE OR REPLACE FUNCTION geo.get_countries(pattern varchar)
       RETURNS SETOF geo.countries
AS $$
    DECLARE match_expr varchar;
    BEGIN
        match_expr = (LOWER(pattern) || '%%');

        RETURN QUERY SELECT c.* FROM geo.countries c
    	       WHERE LOWER(c.ident) LIKE match_expr
	       OR LOWER(c.localized_name) LIKE match_expr
	       OR LOWER(c.code) LIKE match_expr
	       ORDER BY c.ident ASC;
    END;
$$
LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION geo.get_cities(pattern varchar)
       RETURNS SETOF geo.cities
AS $$
    DECLARE match_expr varchar;
    BEGIN
        match_expr = (LOWER(pattern) || '%%');

        RETURN QUERY SELECT c.* FROM geo.cities c
    	       WHERE LOWER(c.ident) LIKE match_expr
	       OR LOWER(c.localized_name) LIKE match_expr
	       OR LOWER(c.code) LIKE match_expr
	       ORDER BY c.ident ASC;
    END;
$$
LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION geo.get_cities(pattern varchar, country varchar)
       RETURNS SETOF geo.cities
AS $$
    DECLARE match_expr varchar;
    DECLARE geo_country_id integer;
    BEGIN
        match_expr = (LOWER(pattern) || '%%');
	IF country IS NULL THEN
	   RETURN;
	ELSE
	   -- NOTE: if more than one matched here - the first one will be used,
	   -- so country arg should preferably contain full country name
	   SELECT id INTO geo_country_id FROM geo.get_countries(country);

	   IF FOUND THEN
	       RETURN QUERY SELECT ct.* FROM geo.cities ct
    	          WHERE ct.country_id = geo_country_id
	          AND (LOWER(ct.ident) LIKE match_expr
	          OR LOWER(ct.localized_name) LIKE match_expr
	          OR LOWER(ct.code) LIKE match_expr)
	          ORDER BY ct.ident ASC;
	   END IF;
	END IF;
    END;
$$
LANGUAGE plpgsql;
