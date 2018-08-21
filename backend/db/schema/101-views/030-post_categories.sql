CREATE OR REPLACE VIEW views.post_categories AS
    WITH RECURSIVE post_categories_tree AS (
        SELECT id, ident, ident::text as category, active FROM storage.post_categories
        WHERE parent_id IS NULL and active = true
    UNION ALL
        SELECT curr.id,
	    curr.ident,
	    (prev.category || '/' || curr.ident)::text as category,
	    curr.active
        FROM storage.post_categories curr 
        JOIN post_categories_tree as prev on curr.parent_id = prev.id
    )
    SELECT * FROM post_categories_tree ORDER BY category;
