# """Задача1: Управление базой данных сотрудников
#
# Ситуация: мы создаем систему для управления информацией о сотрудниках в компании.
# Каждый сотрудник имеет уникальный ID, имя, должность и набор навыков.
#
# Задача: используйте словарь для хранения информации о каждом сотруднике, где ключом будет кортеж,
# содержащий ID и имя, а значением — словарь с должностью и множеством навыков.
#
# Вывести в терминал информацию о каждом сотруднике
# """
#
# employees_dict = {}
# employees_dict[(1, "Alice")] = {"position": "Manager", "skills": {"leadership", "communication"}}
# employees_dict[(2, "Bob")] = {"position": "Developer", "skills": {"python", "databases"}}
# print(employees_dict)
#
# for (employee_id, employee_name), employee_info in employees_dict.items():
#     print(f'Сотрудник {employee_id}: {employee_name}')
#     print(f'Должность: {employee_info['position']}')
#     print(f'Навыки: {', '.join(employee_info['skills'])}')
#     print()

# """
# Задача 2: Управление списком проектов
#
# Ситуация: мы разрабатываем систему для управления проектами в компании.
# Каждый проект имеет уникальный номер,
# название, список участников и их роли в проекте.
#
# Задача: используйте словарь для организации информации о проектах,
# где ключом будет кортеж с номером и названием проекта,
# а значением — словарь с множеством участников и их ролями.
#
# Вывести в терминал информацию о каждом проекте
# """
#
# projects_dict = {
#     (101, "Project Alpha"): {"participants": {"Alice": "Lead", "Bob": "Developer"}},
#     (102, "Project Beta"): {"participants": {"Charlie": "Manager", "Dave": "Analyst"}}
# }
#
# #             key                 value
# for (project_id, project_title), details in projects_dict.items():
#     print(f'Проект {project_id}: {project_title}')
#     participants = details['participants']
#     for name, role in participants.items():
#         print(f'{name} - {role}')
#     print()


# words = ("Python", "Java", "C++", "JavaScript", "Ruby")
# # Вывод количества элементов
# print(f'Количество элементов (длина) кортежа: {len(words)}')
#
# search_word = input("Введите ЯП для поиска: ")
# # Проверка наличия строки
# if search_word in words:
#     print(f'{search_word}, содержится в кортеже.')
# else:
#     print(f'{search_word}, отсутствует в кортеже.')
# # Вывод первого и последнего элемента
# print(f'Первый элемент кортежа: {words[0]}')
# print(f'Последний элемент кортежа: {words[-1]}')


"""Задача: напишите программу, которая использует словарь для управления списком сотрудников и их должностей.
Пользователь может добавлять новых сотрудников,
удалять их по имени и просматривать список всех сотрудников с должностями."""
import random
import string

employees = {}
employees_ids = []

while True:
    user_command = input("Введите команду (add, remove, list, exit)")
    # user_command = input("Выберете команду (1 - add, 2 - remove, 3 - list, 4 - exit)")
    if user_command == 'add':  # if user_command == '1'
        user_choice = input('add - добавить, change - изменить')
        if user_choice == 'add':
            employee_id = ''.join(random.sample(string.digits + string.digits + string.digits, 3))
            while employee_id in employees_ids:
                print('Такой id уже существует')
                employee_id = ''.join(random.sample(string.digits + string.digits + string.digits, 3))
            employees_ids.append(employee_id)
        elif user_choice == 'change':
            employee_id = input('id?: ')
        else:
            continue
        name = input("Введите имя сотрудника: ")
        position = input("Введите должность сотрудника: ")
        employees[employee_id] = [name, position]
        if user_choice == 'add':
            print('Сотрудник добавлен!')
        else:
            print('Сотрудник изменен!')
    elif user_command == 'remove':  # elif user_command == '2'
        name = input("Введите имя сотрудника для удаления: ")
        if name in employees:
            del employees[name]
            print("Сотрудник удален")
        else:
            print("Сотрудник не найден!")
    elif user_command == 'list':  # elif user_command == '3'
        if len(employees) == 0:  # if not employees:
            print('Список сотрудников пуст.')
        else:
            print('Список сотрудников и их должностей')
            for name, data in employees.items():
                print(f'{name}: {data[0]}, {data[1]}')
    elif user_command == 'exit':  # elif user_command == '4':
        break
    else:
        print("Не знаю такой команды")

print(employees_ids)