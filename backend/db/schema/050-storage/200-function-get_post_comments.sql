CREATE OR REPLACE FUNCTION
        storage.get_post_comments_flat(
		_post_id integer
       	) RETURNS SETOF RECORD
AS
$$
    DECLARE record_ RECORD;

BEGIN
    FOR record_ IN
	WITH RECURSIVE post_comments_tree AS (
	    SELECT pc.id, pc.parent_id, 0 as lvl, pc.post_id,
	        pc.user_id, u.active as user_active,
	    	u.username as author, extract('epoch' from pc.ctime)::integer as ctime,
		pc.score,
		CASE WHEN pc.deleted THEN '' ELSE content END,
		pc.deleted,
		CASE WHEN pc.deleted_by IS NOT NULL THEN
		  (SELECT d.username FROM auth.users d WHERE d.id = pc.deleted_by)
		ELSE
		  ''
		END AS deleted_by,
		array[pc.id] as parents_path
	    FROM storage.post_comments pc
	    JOIN auth.users u ON u.id = pc.user_id
	    WHERE pc.post_id = _post_id AND pc.parent_id is null
	UNION ALL
	    SELECT curr.id, curr.parent_id, prev.lvl + 1 as lvl, curr.post_id,
	    	curr.user_id, u2.active as user_active,
	    	u2.username as author, extract('epoch' from curr.ctime)::integer as ctime,
		curr.score,
		CASE WHEN curr.deleted THEN '' ELSE curr.content END,
		curr.deleted,
		CASE WHEN curr.deleted_by IS NOT NULL THEN
		  (SELECT d.username FROM auth.users d WHERE d.id = curr.deleted_by)
		ELSE
		  ''
		END AS deleted_by,
		prev.parents_path || curr.id
	    FROM storage.post_comments curr 
	    JOIN auth.users u2 ON u2.id = curr.user_id
	    JOIN post_comments_tree AS prev ON curr.parent_id = prev.id
	)
	SELECT id, parent_id, lvl, post_id, user_id, user_active,
	       author, ctime, score, content, deleted, deleted_by
	       FROM post_comments_tree pct ORDER BY parents_path
    LOOP
    	RETURN NEXT record_;
    END LOOP;
END;
$$
LANGUAGE plpgsql;
