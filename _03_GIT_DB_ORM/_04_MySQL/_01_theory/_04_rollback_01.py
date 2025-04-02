import sqlite3

if __name__ == '__main__':
    conn = sqlite3.connect(r'data_bases/mydb.db')
    cursor = conn.cursor()
    try:
        cursor.execute("BEGIN TRANSACTION")
        cursor.execute("INSERT INTO users (name) VALUES (?)", ("Ivan",))
        cursor.execute("INSERT INTO users (name) VALUES (?)", ("Petr",))

        raise Exception("Что-то пошло не так!")
        conn.commit()

    except Exception as e:
        conn.rollback()
        print(f"Ошибка: {e}")

    finally:
        conn.close()
