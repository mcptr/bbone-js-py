CREATE OR REPLACE FUNCTION core.set_config_value(ident_ varchar,  value_ boolean)
        RETURNS VOID
AS $$
   BEGIN
      INSERT INTO core.config(ident, option_type, bool_value)
   	  VALUES(ident_, 'BOOL', value_);
      EXCEPTION WHEN unique_violation THEN
        UPDATE core.config SET bool_value = value_ WHERE ident = ident_;
   END;
$$
LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION core.set_config_value(ident_ varchar,  value_ integer)
       RETURNS VOID
AS $$
   BEGIN
      INSERT INTO core.config(ident, option_type, int_value)
   	  VALUES(ident_, 'INT', value_);
      EXCEPTION WHEN unique_violation THEN
        UPDATE core.config SET int_value = value_ WHERE ident = ident_;
   END;
$$
LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION core.set_config_value(ident_ varchar,  value_ numeric)
       RETURNS VOID
AS $$
   BEGIN
      INSERT INTO core.config(ident, option_type, double_value)
   	  VALUES(ident_, 'NUMERIC', value_);
      EXCEPTION WHEN unique_violation THEN
        UPDATE core.config SET double_value = value_ WHERE ident = ident_;
   END;
$$
LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION core.set_config_value(ident_ varchar,  value_ varchar)
       RETURNS VOID
AS $$
   BEGIN
      INSERT INTO core.config(ident, option_type, string_value)
   	  VALUES(ident_, 'STRING', value_);
      EXCEPTION WHEN unique_violation THEN
        UPDATE core.config SET string_value = value_ WHERE ident = ident_;
   END;
$$
LANGUAGE plpgsql;
