import re

# text = '<div>Первый</div><div>Второй</div>'
# pattern = re.compile(r'<div>.*</div>')
# matches = re.findall(pattern, text)
# print(matches)

text = '<div>Первый</div><div>Второй</div>'
pattern = re.compile(r'<div>.*?</div>')
matches = re.findall(pattern, text)
print(matches)