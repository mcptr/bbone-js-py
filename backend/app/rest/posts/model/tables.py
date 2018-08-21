from app import db

posts = db.inspect_table("posts", schema="views")
comments = db.inspect_table("post_comments", schema="storage")
categories = db.inspect_table("post_categories", schema="storage")
channels = db.inspect_table("post_channels", schema="storage")
votes = db.inspect_table("post_votes", schema="storage")
tags_map = db.inspect_table("posts_tags_map", schema="storage")
