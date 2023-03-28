-- script that lists all shows contained in the database hbtn_0d_tvshows

SELECT t.title, tv.genre_id
FROM tv_shows AS t
LEFT JOIN tv_show_genres AS tv
WHERE t.id = tv.show_id
ORDER BY t.title, tv.genre_id;
