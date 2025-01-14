from module_12_01 import push, pop

stack = []

while True:
    command = input("Введите команду (1 - add, 2 - complete, 3 - show, 4 - exit): ")
    if command == '1':
        task = input("Введите задачу: ")
        push(stack, task)
        print(f'Задача "{task}" добавлена.')

    elif command == '2':
        completed = pop(stack)
        if completed:
            print(f'Задача "{completed}" завершена!')

    elif command == '3':
        if stack:
            print(stack)
        else:
            print("Нет задач для завершения.")

    elif command == '4':
        print('Работа завершена')
        break

    else:
        print("Неизвестная команда!")
