#
# if __name__ == '__main__':
#     # получение данных
#     session.query(User).filter_by(name="Алиса").first()
#
#     # добавить нового пользователя (НЕОБХОДИМА МОДЕЛЬ!!!!)
#     new_user = User(name="Боб", email="bob@example.com")
#     session.add(new_user)
#     session.commit()
#
#     # обновить данные
#     user = session.query(User).filter_by(name="Боб").first()
#     user.email = "bob_new@example.com"
#     session.commit()
#
#     # удалить запись
#     user = session.query(User).filter_by(name="Боб").first()
#     session.delete(user)
#     session.commit()
