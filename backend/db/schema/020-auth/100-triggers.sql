CREATE FUNCTION auth.trg_hash_password() RETURNS trigger
    LANGUAGE plpgsql
AS $$
    BEGIN
        IF substr(NEW.password, 1, 3) <> '$1$' THEN
            NEW.password := crypt(NEW.password, gen_salt('md5'));
        END IF;
        RETURN NEW;
    END;
$$;

CREATE FUNCTION auth.trg_lc_username() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
DECLARE
BEGIN
    NEW.username := LOWER(NEW.username);
    RETURN NEW;
END;
$$;


-- users

CREATE TRIGGER trg_hash_password BEFORE INSERT OR UPDATE ON auth.users
       FOR EACH ROW EXECUTE PROCEDURE auth.trg_hash_password();

CREATE TRIGGER trg_lc_username BEFORE INSERT OR UPDATE ON auth.users
       FOR EACH ROW EXECUTE PROCEDURE auth.trg_lc_username();

CREATE TRIGGER trg_lc_ident BEFORE INSERT OR UPDATE ON auth.users
       FOR EACH ROW EXECUTE PROCEDURE generic.trg_lc_ident();

CREATE TRIGGER trg_update_mtime BEFORE INSERT OR UPDATE ON auth.users
       FOR EACH ROW EXECUTE PROCEDURE generic.trg_update_mtime();

-- groups

CREATE TRIGGER trg_lc_ident BEFORE INSERT OR UPDATE ON auth.groups
       FOR EACH ROW EXECUTE PROCEDURE generic.trg_lc_ident();

