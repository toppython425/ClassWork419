import sqlite3
from _SQLQueries import _01_SQL_QUERIES


class SQLiteConnector:
    def __init__(self, path):
        self.conn = sqlite3.connect(path)
        self.cursor = self.conn.cursor()
        # self.conn.autocommit = True

    def execute_query(self, query):
        self.cursor.execute(query)


if __name__ == '__main__':
    conn_obj_example = SQLiteConnector(r'data_bases/example.db')
    try:
        conn_obj_example.cursor.execute("""
        CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER
        )
        """)
    except sqlite3.Error as er:
        print(er)

    # conn_obj_example.cursor.execute(_01_SQL_QUERIES.create_table("users1"))
    # conn_obj_example.execute_query(_01_SQL_QUERIES.create_table("users2"))
    conn_obj_example.conn.commit()
