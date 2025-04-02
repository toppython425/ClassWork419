import sqlite3


if __name__ == '__main__':
    conn = sqlite3.connect(r'databases/my_database.db')
    cursor = conn.cursor()

    # Таблица пользователей
    cursor.execute("""
        DROP TABLE orders 
        """)

    cursor.execute("""
            DROP TABLE users 
            """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT
    )
    """)

    # Таблица заказов, где каждый заказ связан с пользователем (user_id)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        item TEXT,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
    """)

    conn.commit()

    # Добавляем пользователей
    cursor.execute("INSERT INTO users (name) VALUES (?)", ("Алиса",))
    cursor.execute("INSERT INTO users (name) VALUES (?)", ("Боб",))
    conn.commit()

    # Добавляем заказы, указывая user_id
    cursor.execute("INSERT INTO orders (user_id, item) VALUES (?, ?)", (1, "Ноутбук"))
    cursor.execute("INSERT INTO orders (user_id, item) VALUES (?, ?)", (1, "Телефон"))
    cursor.execute("INSERT INTO orders (user_id, item) VALUES (?, ?)", (2, "Часы"))
    conn.commit()

    cursor.execute("""
    SELECT users.name, orders.item
    FROM users
    JOIN orders ON users.id = orders.user_id
    WHERE users.id = ?
    """, (1,))

    orders = cursor.fetchall()
    conn.close()
    print(orders)

