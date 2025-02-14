import re

text = "Серверы доступны по адресам: 192.168.1.1, 256.256.256.256, 127.0.0.1, 0.0.0.0, 100.100.100.100."

pattern = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')
pattern1 = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
# pattern1 = re.compile(r'(\d{1,3}\.){3}\d{1,3}')

ip_addresses = re.findall(pattern1, text)
print(ip_addresses)

valid_ips = []
for ip in ip_addresses:
    parts = ip.split('.')
    print(parts)
    if all(0 <= int(part) <= 255 for part in parts):
        valid_ips.append(ip)

print('Корректные IP-адреса', valid_ips)
