CREATE TABLE storage.posts_tags_map (
    id bigserial primary key,
    post_id integer NOT NULL references storage.posts(id),
    tag_id integer NOT NULL references storage.tags(id)
);

CREATE UNIQUE INDEX posts_tags_map_uidx on storage.posts_tags_map(post_id, tag_id);
