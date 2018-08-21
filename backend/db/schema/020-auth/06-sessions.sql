CREATE TABLE auth.sessions (
       id varchar(64) PRIMARY KEY,
       ctime timestamp NOT NULL DEFAULT NOW(),
       mtime timestamp NOT NULL DEFAULT NOW(),
       user_id INTEGER DEFAULT NULL REFERENCES auth.users(id) ON UPDATE CASCADE ON DELETE CASCADE,
       permanent BOOLEAN default FALSE,
       client_agent VARCHAR(255) DEFAULT NULL,
       client_origin VARCHAR(64) DEFAULT NULL,
       social_access_token varchar(512) DEFAULT NULL,
       -- FIXME: change to jsonb with postgres 9.4
       data json DEFAULT NULL
);

CREATE TRIGGER trg_update_mtime BEFORE INSERT OR UPDATE ON auth.sessions
       FOR EACH ROW EXECUTE PROCEDURE generic.trg_update_mtime();
