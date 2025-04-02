import sqlite3

if __name__ == '__main__':
    conn = sqlite3.connect(r'data_bases/mydb.db')
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER
    );
    """)

    conn.commit()
    conn.close()
