import requests

response = requests.get('https://jsonplaceholder.typicode.com/users/1/todos')

if response.status_code == 200:
    todos = response.json()
    print(todos)
    for task in todos:
        if task['completed']:
            print(f'Задача {task['id']}: {task['title']} - выполнена')
        else:
            print(f'Задача {task['id']}: {task['title']} -  не выполнена')
        # print(f"Задача {task['id']}: {task['title']} - {'Выполнена' if task['completed'] else 'Не выполнена'}")
else:
    print(f'Ошибка: {response.status_code}')
