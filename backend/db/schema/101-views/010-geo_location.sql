CREATE VIEW views.geo_location AS
 SELECT ct.ident AS city,
    ct.localized_name AS localized_city,
    ct.code AS city_code,
    cnt.ident AS country,
    cnt.localized_name AS localized_country,
    cnt.code AS country_code
   FROM geo.cities ct
     LEFT JOIN geo.countries cnt ON ((ct.country_id = cnt.id))
  ORDER BY cnt.ident, ct.ident;
