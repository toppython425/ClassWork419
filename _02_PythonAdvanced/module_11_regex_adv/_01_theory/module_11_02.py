import re

# text = "Контактный номер: 81234567890."
# pattern = r'8\d{10}'
# matches = re.findall(pattern, text)
# print(matches)


text = "Контактные номера: +7 (123) 456-78-90, 81234567890 и 8-123-456-78-90."
pattern = re.compile(r'\+?\d[\d\s\-()]{10,15}')
matches = re.findall(pattern, text)
print(matches)
