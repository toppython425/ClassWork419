import sqlite3

if __name__ == '__main__':
    # TASK 1
    conn = sqlite3.connect(r'database/users.db')
    cursor = conn.cursor()
    cursor.execute("DROP TABLE users")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    email TEXT NOT NULL
    );
    """)
    conn.commit()

    users = [
        ('Иван Иванов', 28, 'ivan@example.com'),
        ('Мария Смирнова', 34, 'maria@example.com'),
        ('Петр Петров', 22, 'peter@example.com'),
        ('Алексей Иванов', 25, 'alexey@example.com'),
        ('Ольга Сидорова', 29, 'olga@example.com')
    ]

    # for user in users:
    #     cursor.execute("INSERT INTO users (name, age, email) VALUES (?, ?, ?)", user)

    cursor.executemany('''
    INSERT INTO users (name, age, email) VALUES (?, ?, ?)
    ''', users)

    conn.commit()

    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    for user in users:
        print(user)
    print()

    cursor.execute("SELECT name, age, email FROM users WHERE age > 25")
    filtered_users = cursor.fetchall()
    for user in filtered_users:
        print(user)

    conn.close()
    print()

    # TASK 2
    print("TASK2")

    conn = sqlite3.connect(r'database/users.db')
    cursor = conn.cursor()
    cursor.execute("""
    UPDATE users
    SET age = age + 2
    WHERE user_id = 1
    """)

    cursor.execute("""
        UPDATE users
        SET age = age + 3
        WHERE user_id = 4
        """)

    conn.commit()

    cursor.execute("""
        DELETE FROM users
        WHERE age < 25
    """)

    conn.commit()

    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    for user in users:
        print(user)

    conn.close()


