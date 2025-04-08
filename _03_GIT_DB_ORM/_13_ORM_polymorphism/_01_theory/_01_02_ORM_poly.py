class Field:

    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return f'{self.name}: {self.column_type}'


class IntegerField(Field):
    def __init__(self, name):
        super().__init__(name, 'integer')


class StringField(Field):
    def __init__(self, name):
        super().__init__(name, 'varchar(255)')


class ModelMeta(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return super().__new__(cls, name, bases, attrs)

        fields = {}
        for key, value in attrs.items():
            if isinstance(value, Field):
                fields[key] = value

        attrs['_fields'] = fields
        return super().__new__(cls, name, bases, attrs)


class Model(metaclass=ModelMeta):
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def save(self):
        fields = []
        values = []
        for name, field in self._fields.items():
            fields.append(field.name)
            values.append(getattr(self, name, None))

        sql = f'INSERT INTO {self.__class__.__name__.lower()} ({', '.join(fields)}) VALUES ({', '.join(['%s'] * len(values))})'
        print(f'Выполняется SQL: {sql} c параметрами {values}')


class User(Model):
    id = IntegerField('id')
    name = StringField('name')


if __name__ == '__main__':
    user = User(id=1, name='John')
    user.save()
