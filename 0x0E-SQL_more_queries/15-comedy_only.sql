-- script that lists all Comedy shows in the database hbtn_0d_tvshows

SELECT tvs.title
FROM tv_shows AS tvs
INNER JOIN tv_show_genres AS tvs
ON tvs.id = tvs.show_id

INNER JOIN tv_genres AS tvg
ON tvg.id = tvs.genre_id
WHERE tvg.name = "Comedy"
ORDER BY tvs.title ASC;
