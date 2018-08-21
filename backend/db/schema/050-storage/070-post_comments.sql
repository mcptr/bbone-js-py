CREATE TABLE storage.post_comments (
    id bigserial primary key,
    post_id integer default null references storage.posts(id) on update cascade on delete cascade,
    parent_id bigint default null references storage.post_comments(id) on update cascade on delete cascade,
    user_id integer NOT NULL references auth.users(id) on update cascade on delete cascade,
    score integer not null default 0,
    content TEXT NOT NULL,
    deleted boolean not null default false,
    deleted_by integer default null references auth.users(id) on update cascade on delete no action,
    ctime timestamp without time zone default now() not null,
    mtime timestamp without time zone default now() not null
);

create index post_comments_post_id_idx on storage.post_comments(post_id);
