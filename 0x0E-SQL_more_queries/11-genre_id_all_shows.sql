-- Retrieves show titles and genre IDs, including shows without linked genres
SELECT tv_shows.title, IFNULL(tv_show_genres.genre_id, 'N/A') AS genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, genre_id ASC;
