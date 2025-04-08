import requests

headers = {
    'Content-Type': 'application/json'
}

data = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=data,
    headers=headers,
)

print(response.status_code)
print(response.json())
