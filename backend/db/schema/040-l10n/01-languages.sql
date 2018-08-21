create table l10n.languages (
       id serial primary key,
       iso_code char(2) not null unique,
       ident varchar(64) not null
);
