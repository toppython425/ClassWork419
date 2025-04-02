# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS users (
#         id INTEGER PRIMARY KEY,
#         name TEXT
#     )
#     """)

# # неверные имена полей при создании таблиц с внешним ключом
# cursor.execute("""
# CREATE TABLE orders (
#     id INTEGER PRIMARY KEY,
#     user_id INTEGER,
#     item TEXT,
#     FOREIGN KEY (user_id) REFERENCES users(uid)  -- Ошибка: users.uid не существует
# )
# """)


# # убедитесь что ключ ссылается на существующе в таблице поля
# cursor.execute("""
# CREATE TABLE orders (
#     id INTEGER PRIMARY KEY,
#     user_id INTEGER,
#     item TEXT,
#     FOREIGN KEY (user_id) REFERENCES users(id)  -- Теперь ссылка корректная
# )
# """)
