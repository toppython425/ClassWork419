from SimpleORM import SimpleORM

if __name__ == '__main__':
    orm = SimpleORM(r'database/example.db')
    print(orm.select('users', age=30))
    print()

    orm.update(table_name='users', set_data={'age': 31}, name='Alice')
    print(orm.select('users', age=31))
    print()

    orm.delete(table_name='users', name='Bob')
    print(orm.select('users'))