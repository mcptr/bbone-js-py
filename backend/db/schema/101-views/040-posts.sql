CREATE OR REPLACE VIEW views.posts AS
    SELECT 
       p.id,
       p.category_id,
       p.user_id,
       p.title,
       p.description,
       p.language_id,
       p.content_type::TEXT,
       p.src_url,
       p.thumbnail_url,
       p.stat_views,
       p.stat_votes_plus,
       p.stat_votes_minus,
       p.stat_anon_votes_plus,
       p.stat_anon_votes_minus,
       (select count(id) from storage.post_comments pcm where pcm.post_id = p.id) AS stat_total_comments,
       p.channel_id,
       extract('epoch' from p.ctime) AS ctime,
       extract('epoch' from p.mtime) AS mtime,
       l.iso_code AS language_code,
       l.ident AS language_name,
       u.username as author,
       (select ch.ident from storage.post_channels ch where ch.id = p.channel_id) as channel,
       (select pc.ident from views.post_categories pc WHERE pc.id = p.category_id) as category,
       array(SELECT t.ident FROM storage.tags t WHERE t.id IN 
          (SELECT ptm.tag_id FROM storage.posts_tags_map ptm WHERE ptm.post_id = p.id)
       ) AS tags
       FROM storage.posts p
       JOIN auth.users u ON u.id = p.user_id
       LEFT JOIN l10n.languages l ON p.language_id = l.id
       ORDER BY p.id desc, p.ctime desc, p.id desc, p.stat_votes_plus desc, p.stat_views desc, p.stat_anon_votes_plus desc;
