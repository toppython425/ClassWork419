from SimpleORM import SimpleORM

if __name__ == '__main__':
    orm = SimpleORM(r'database/example.db')
    orm.create_table(table_name='users', name='TEXT', age='INTEGER')
    print()

    users = [
        {'name': 'Alice', 'age': 25},
        {'name': 'Bob', 'age': 30},
    ]
    for user in users:
        orm.insert(table_name='users', name=user['name'], age=user['age'])
    print()

    print(orm.select(table_name='users'))

