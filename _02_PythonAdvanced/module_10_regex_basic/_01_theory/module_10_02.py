import re

text = "Мой телеграм - @username. Но лучше свяжитесь со мной по email: user@example.com или support@domain.org."

pattern = re.compile(r'[\w.-]+@[\w.-]+')
matches = re.findall(pattern, text)
print(matches)

pattern = re.compile(r'[\w.-]+@example\.com')
matches = re.findall(pattern, text)
print(matches)