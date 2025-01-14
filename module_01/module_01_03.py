user_name = input("Введите ваше имя: ")
print("Привет!", user_name)

cost_input = input("Введите стоимость товара, только целое число: ")
cost = int(cost_input)
print(type(cost))

cost_input_1 = int(input("Введите стоимость товара, только целое число: "))
#                    после enter в int() попадает сразу то что мы ввели
print(type(cost_input_1))

user_name = input("Введите ваше имя: ")
print("Привет! {user_name}!")

user_name = input("Введите ваше имя: ")
print("Привет!", user_name, "!")

user_name = input("Введите ваше имя: ")
print(f"Привет! {user_name}!")

discount = 20.5
total_amount = 150.75

formatted_string = f'Ваша скидка составила ${discount:.2f}. Итоговая сумма ${total_amount:.2f}'
print(formatted_string)
