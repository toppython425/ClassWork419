import sqlite3

if __name__ == '__main__':
    conn = sqlite3.connect(r'data_bases/students.db')
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM students WHERE age > ?", (21,))
        cursor.execute("SELECT * FROM students")
        young_studs = cursor.fetchall()
    except sqlite3.Error as err:
        print(err)
    else:
        print(young_studs)
        conn.commit()
    finally:
        conn.close()
