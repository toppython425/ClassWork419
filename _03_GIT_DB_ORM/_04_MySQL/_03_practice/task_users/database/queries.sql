CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    email TEXT NOT NULL
    );


SELECT name, COUNT(*) AS book_count
FROM biblia
GROUP BY name
HAVING COUNT(*) = (
    SELECT MAX(book_count) FROM (
        SELECT COUNT(*) AS book_count FROM biblia GROUP BY name
        )
    )


SELECT name, COUNT(*) AS book_count
FROM biblia
GROUP BY name
ORDER BY book_count DESC
LIMIT 1;