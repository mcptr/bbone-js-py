CREATE OR REPLACE VIEW views.tags_popularity AS
	SELECT t.ident, COUNT(ptm.post_id) as score
	FROM storage.posts_tags_map ptm
	JOIN storage.tags t ON t.id = ptm.tag_id AND t.active = TRUE
	GROUP BY ptm.tag_id, t.ident
	ORDER BY score desc, t.ident asc;
