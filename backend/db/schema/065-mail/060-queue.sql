CREATE TABLE mail.queue (
       id bigserial PRIMARY KEY,
       message_id INTEGER NOT NULL REFERENCES mail.messages(id),
       recipient_id INTEGER NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE ON UPDATE CASCADE,
       sender VARCHAR(512) DEFAULT NULL,
       sent BOOLEAN DEFAULT FALSE,
       success BOOLEAN DEFAULT FALSE,
       delivery_failures INTEGER DEFAULT 0,
       delivery_time TIMESTAMP DEFAULT NULL,
       ctime TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE UNIQUE INDEX mail_queue_uidx ON mail.queue(message_id, recipient_id);
