import requests

# requests.post(
#     "https://api.example.com",
#     json={"key": "value"},
# )
#
# requests.get("https://api.example.com?api_key=123")


requests.post(
    "https://api.example.com",
    json={"key": "value"},
    headers={
        'content-type': 'application/json',
        'Authorisation': 'YOUR_API_KEY'
    }
)

requests.get("https://api.example.com?api_key=123")
