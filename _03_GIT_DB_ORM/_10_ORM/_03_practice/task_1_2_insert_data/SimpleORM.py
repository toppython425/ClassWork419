import sqlite3

class SimpleORM:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_table(self, table_name, **columns):
        columns_with_types = ', '.join([f'{col} {dtype}' for col, dtype in columns.items()])
        print(columns_with_types)
        self.cursor.execute(f'CREATE TABLE IF NOT EXISTS {table_name} (id INTEGER PRIMARY KEY, {columns_with_types})')
        self.conn.commit()

    def insert(self, table_name, **data):
        columns = ', '.join(data.keys())
        placeholders = ', '.join(['?'] * len(data))
        print(columns)
        print(placeholders)
        self.cursor.execute(f'INSERT INTO {table_name} ({columns}) VALUES ({placeholders})', tuple(data.values()))
        self.conn.commit()

    def select(self, table_name, **conditions):
        query = f'SELECT * FROM {table_name}'
        if conditions:
            query += ' WHERE ' + ' AND '.join([f'{col} = ?' for col in conditions.keys()])
            print(query)
            self.cursor.execute(query, tuple(conditions.values()))
        else:
            print(query)
            self.cursor.execute(query)
        return self.cursor.fetchall()

    def update(self, table_name, set_data, **conditions):
        set_clause = ', '.join([f'{col} = ?' for col in set_data.keys()])
        query = f'UPDATE {table_name} SET {set_clause}'
        if conditions:
            query += ' WHERE ' + ' AND '.join([f'{col} = ?' for col in conditions.keys()])
            print(query)
            self.cursor.execute(query, tuple(list(set_data.values()) + list(conditions.values())))
        else:
            print(query)
            self.cursor.execute(query, tuple(set_data.values()))
        self.conn.commit()

    def delete(self, table_name, **conditions):
        query = f'DELETE FROM {table_name}'
        if conditions:
            query += ' WHERE ' + ' AND '.join([f'{col} = ?' for col in conditions.keys()])
            print(query)
            self.cursor.execute(query, tuple(conditions.values()))
        else:
            print(query)
            self.cursor.execute(query)
        self.conn.commit()

    def __del__(self):
        self.conn.close()