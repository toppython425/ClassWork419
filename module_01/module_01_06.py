# user_name = input("Введите ваше имя: ")
# user_balance_input = input("Введите ваш начальный баланс: ")
# user_balance = float(user_balance_input)
#
# if user_balance < 0:
#     print("Начальный баланс не может быть отрицательным!")
# else:
#     print(f"Добро пожаловать, {user_name}! Ваш начальный баланс: {user_balance:.2f} руб.")


# card_number = input("Введите номер вашей скидочной карты: ")
card_number = "102345"
discount_input = input("Введите размер вашей скидки в процентах: ")
discount = float(discount_input)

if discount < 0 or discount > 100:
    print("Размер скидки должен быть между 0% и 100%")
else:
    print(f'Карта №{card_number} активирована. Ваша скидка: {discount:.2f}%.')

if 0 <= discount <= 100:
    print(f'Карта №{card_number} активирована. Ваша скидка: {discount:.2f}%.')
else:
    print("Размер скидки должен быть между 0% и 100%")
