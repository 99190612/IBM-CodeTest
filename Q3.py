# SET @different_category_count = 
# (SELECT COUNT(article_id), ownerid FROM article
# INNER JOIN category_article_mapping ON article.article_id = category_article_mapping.article_id
# GROUP BY article.ownerid);

# SELECT @different_category_count = different_category_count, owner_id, owner_name
# FROM owner 
# ORDER BY different_category_count DESC;