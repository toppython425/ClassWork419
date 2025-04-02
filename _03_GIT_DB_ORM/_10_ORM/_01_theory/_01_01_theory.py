# user = User(name="Алиса", age=25, password=set_password('password'))
# user.save()
#
# engine = create_engine("sqlite:///example.db")  # SQLite
# # Или
# engine = create_engine("postgresql://user:password@localhost/dbname")  # PostgreSQL
#
#
# user = session.query(User).filter_by(name="Алиса").first()
#
# user.age