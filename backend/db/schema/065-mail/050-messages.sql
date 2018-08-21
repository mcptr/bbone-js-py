CREATE TABLE mail.messages(
       id serial PRIMARY KEY,
       title VARCHAR(255) NOT NULL,
       body_text TEXT,
       body_html TEXT,
       ctime TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, 
       mtime TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
