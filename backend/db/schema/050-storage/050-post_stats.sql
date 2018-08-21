create table storage.post_votes (
    id bigserial primary key,
    post_id integer not null references storage.posts(id) on update cascade on delete cascade,
    user_id integer not null references auth.users(id) on update cascade on delete cascade,
    is_upvote boolean not null,
    kill_reason types.post_kill_reason not null default 'OTHER',
    ctime timestamp without time zone default now() not null,
    mtime timestamp without time zone default now() not null
);

create unique index user_post_vote_uidx on storage.post_votes(post_id, user_id);
