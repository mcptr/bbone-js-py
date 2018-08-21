CREATE TABLE auth.user_group_map (
    id serial primary key,
    user_id integer NOT NULL references auth.users(id) on update cascade on delete cascade,
    group_id integer NOT NULL references auth.groups(id) on update cascade on delete cascade,
    ctime timestamp without time zone DEFAULT now() NOT NULL
);

create unique index user_group_map_uidx on auth.user_group_map(user_id, group_id);
