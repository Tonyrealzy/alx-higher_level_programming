-- script that lists all shows contained in hbtn_0d_tvshows
-- that have at least one genre linked

SELECT t.title, tv.genre_id
FROM tv_shows as t
INNER JOIN tv_show_genres as tv
ON t.id = tv.show_id
ORDER BY t.title, tv.genre_id ASC
