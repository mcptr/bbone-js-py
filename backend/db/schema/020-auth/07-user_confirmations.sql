CREATE TABLE auth.user_confirmations(
       id SERIAL NOT NULL primary key,
       confirmation_key VARCHAR(255) NOT NULL,
       user_id INTEGER NOT NULL REFERENCES auth.users(id) ON UPDATE CASCADE ON DELETE CASCADE,
       action_type VARCHAR(128) NOT NULL,
       max_age INTEGER NOT NULL DEFAULT 604800,
       ctime TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
       confirmed_on TIMESTAMP DEFAULT NULL
);

CREATE UNIQUE INDEX user_confirmations_uidx
       ON auth.user_confirmations(user_id, action_type);
