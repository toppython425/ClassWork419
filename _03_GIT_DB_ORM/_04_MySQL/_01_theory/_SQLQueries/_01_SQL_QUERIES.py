def create_table(name):
    SQLQuery = fr"""
    CREATE TABLE IF NOT EXISTS {name} (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER
    )
    """
    return SQLQuery
