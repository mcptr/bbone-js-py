CREATE FUNCTION generic.trg_lc_ident() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
DECLARE
BEGIN
    NEW.ident := lower(NEW.ident);
    RETURN NEW;
END;
$$;


CREATE FUNCTION generic.trg_uc_ident() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
DECLARE
BEGIN
    NEW.ident := upper(NEW.ident);
    RETURN NEW;
END;
$$;


CREATE FUNCTION generic.trg_initcap_ident() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
DECLARE
BEGIN
    NEW.ident := initcap(NEW.ident);
    RETURN NEW;
END;
$$;


CREATE FUNCTION generic.trg_update_mtime() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
DECLARE
BEGIN
    NEW.mtime := NOW();
    RETURN NEW;
END;
$$;

CREATE FUNCTION generic.trg_uc_code() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
DECLARE
BEGIN
    NEW.code := upper(NEW.code);
    RETURN NEW;
END;
$$;

CREATE FUNCTION generic.trg_lc_code() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
DECLARE
BEGIN
    NEW.code := LOWER(NEW.code);
    RETURN NEW;
END;
$$;
