import re

text = "Мой номер телефона: +7 (123) 456-78-90. Также можно связаться по номеру +7 (987) 654-32-10. +375(172)666-55-44"
pattern = re.compile(r'\+\d{1,3}\s?\(\d{3}\)\s?\d{3}-\d{2}-\d{2}')
phone_numbers = re.findall(pattern, text)
print(f"Найденные телефонные номера: {phone_numbers}")
