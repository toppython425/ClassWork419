import requests

new_task = {
    'userId': 1,
    'title': 'Купить молоко',
    'completed': False
}

response = requests.post(
    'https://jsonplaceholder.typicode.com/todos',
    json=new_task
)

print(f'Статус: {response.status_code}')
print(response.json())
