-- Retrieves titles and their total rating from tv_show_ratings
SELECT tv_shows.title, COALESCE(SUM(tv_show_ratings.rate), 0) AS 'rating'
FROM tv_shows
LEFT JOIN tv_show_ratings ON tv_show_ratings.show_id = tv_shows.id
GROUP BY tv_shows.title
ORDER BY rating DESC;
