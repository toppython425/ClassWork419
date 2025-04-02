import sqlite3

"""
Задача: создайте базу данных для хранения информации о книгах и их авторах. 
Напишите SQL-запрос, который выбирает все книги определённого автора.
"""

conn = sqlite3.connect(r'database/Book.db')
cursor = conn.cursor()
cursor.execute("""DROP TABLE biblia""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS  biblia (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        autor TEXT NOT NULL,
        name TEXT NOT NULL,
        [date] INTEGER NOT NULL
    );
""")

books_data = [
    ("1984", "Джордж Оруэлл", 1949),
    ("Мастер и Маргарита", "Михаил Булгаков", 1966),
    ("Преступление и наказание", "Фёдор Достоевский", 1866),
    ("Собачье сердце", "Михаил Булгаков", 1925)
]

cursor.executemany("""
    INSERT INTO biblia (autor, name, [date]) VALUES (?, ?, ?)""", books_data
                   )

conn.commit()

cursor.execute("""
    SELECT * FROM biblia
""")

result = cursor.fetchall()

print(result)
print()

cursor.execute("""
SELECT name, COUNT(*) AS book_count
FROM biblia
GROUP BY name
HAVING COUNT(*) = (
    SELECT MAX(book_count) FROM (
        SELECT COUNT(*) AS book_count FROM biblia GROUP BY name
        )
    )""")
print()

# cursor.execute("""
# SELECT name, COUNT(*) AS book_count
# FROM biblia
# GROUP BY name
# ORDER BY book_count DESC
# LIMIT 1;""")

results = cursor.fetchall()
for row in results:
    print(row)

conn.close()
