import sqlite3

if __name__ == '__main__':
    conn = sqlite3.connect(r'data_bases/students.db')
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM students")
        studs = cursor.fetchmany(2)

    except sqlite3.Error as err:
        print(err)
    else:
        print(studs)
    finally:
        conn.close()

