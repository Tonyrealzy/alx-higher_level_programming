--  script that uses the hbtn_0d_tvshows database
-- to lists all genres of the show Dexter

SELECT tvg
FROM tv_genres
INNER JOIN tv_show_genres AS tvs
ON tvg.id = tvs.genre_id

INNER JOIN tv_shows AS tv
ON tv.id = tvs.show_id
WHERE tv.title = "Dexter"
ORDER BY tvg ASC;
