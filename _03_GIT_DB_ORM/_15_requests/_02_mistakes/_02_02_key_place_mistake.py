import os

import requests
from dotenv import load_dotenv

load_dotenv()

# Ключ в URL — уязвимость безопасности!
requests.get("https://api.example.com/data?api_key=123")

YOUR_API_KEY = os.getenv('API_KEY')

requests.get(
    "https://api.example.com/data",
    headers={"Authorization": f"Bearer {YOUR_API_KEY}"}  # Безопасный способ
)