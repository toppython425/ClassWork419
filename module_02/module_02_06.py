while True:
    try:
        number_of_transactions = int(input('Введите количество транзакций, которое вы хотите добавить: '))
        if number_of_transactions >= 0:
            break
        else:
            print('Количество транзакций не может быть отрицательным. Попробуйте снова.')
    except ValueError:
        print("Неверный ввод! Пожалуйста, введите целое число.")

for i in range(number_of_transactions):
    while True:
        try:
            amount = float(input("Введите сумму транзакции: "))
            if amount >= 0:
                break
            else:
                print("Сумма не может отрицательной. Пожалуйста введите положительное значение.")
        except ValueError:
            print("Неверный ввод! Пожалуйста, введите числовое значение суммы.")
    description = input("Введите описание транзакции: ")
    print(f"Введена транзакция: Сумма - {amount}, Описание - '{description}'")
