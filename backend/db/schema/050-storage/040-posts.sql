CREATE TABLE storage.posts (
    id bigserial primary key,
    category_id integer NOT NULL references storage.post_categories(id) on update cascade on delete cascade,
    user_id integer NOT NULL references auth.users(id) on update cascade on delete cascade,
    title character varying(255) default null::character varying,
    description varchar(1024) default null,
    content text,
    content_type types.post_content_type not null,
    language_id integer default null references l10n.languages(id) on update cascade on delete cascade, 
    src_url character varying(2048) default null::character varying,
    thumbnail_url character varying(1024) default null::character varying,
    channel_id integer DEFAULT NULL references storage.post_channels(id) on update cascade on delete cascade,
    ctime timestamp without time zone default now() not null,
    mtime timestamp without time zone default now() not null,
    stat_views integer not null default 0,
    stat_votes_plus integer not null default 0,
    stat_votes_minus integer not null default 0,
    stat_anon_votes_plus integer not null default 0,
    stat_anon_votes_minus integer not null default 0
);

CREATE TRIGGER trg_update_mtime BEFORE INSERT OR UPDATE ON storage.posts
       FOR EACH ROW EXECUTE PROCEDURE generic.trg_update_mtime();
