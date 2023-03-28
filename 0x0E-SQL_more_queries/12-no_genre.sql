-- script that lists all shows contained in hbtn_0d_tvshows without a genre linked

SELECT t.title, tv.genre_id
FROM tv_shows AS t
LEFT OUTER JOIN tv_show_genres AS tv
ON t.id = tv.show_id
WHERE tv.genre_id IS NULL
ORDER BY t.title, tv.genre_id;
