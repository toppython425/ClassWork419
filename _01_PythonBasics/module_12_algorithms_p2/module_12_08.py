from collections import deque

queue = deque()

while True:
    command = input("Введите команду (1 - add, 2 - serve, 3 - show, 4 - exit): ")
    if command == '1':
        customer = input("Введите имя покупателя: ")
        queue.append(customer)
        print("Покупатель добавлен в очередь.")

    elif command == '2':
        if queue:
            served = queue.popleft()
            print(f'Покупатель {served} обслужен.')
        else:
            print("Очередь пуста!")

    elif command == '3':
        if queue:
            print(', '.join(list(queue)))
        else:
            print("Очередь пуста!")

    elif command == '4':
        print('Работа завершена')
        break

    else:
        print("Неизвестная команда!")
