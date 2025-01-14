import os

if os.path.exists(r'files\appended_data.txt'):
    with open(r'files\appended_data.txt', 'rt', encoding='utf-8') as file:
        content = file.read()
        print(content)
else:
    print("Файл не найден")


if os.path.exists(r'files\appended_data.txt'):
    with open(r'files\appended_data.txt', 'a', encoding='utf-8') as file:
        content = file.write('New data\n')
else:
    print("Файл не найден")

if os.path.exists(r'files\appended_data.txt'):
    file = open(r'files\appended_data.txt', 'r', encoding='utf-8')
    file.close()


if os.path.exists(r'files\appended_data.txt'):
    with open(r'files\appended_data.txt', 'a', encoding='utf-8') as file:
        content = file.write(str(1234))
else:
    print("Файл не найден")
print()

if os.path.exists(r'files\appended_data.txt'):
    with open(r'files\appended_data.txt', 'r+', encoding='utf-8') as file:
        content = file.read()
        print(content)
else:
    print("Файл не найден")
print()

with open(r'files\appended_data.txt', 'r', encoding='utf-8') as file:
    for line in file:
        print(line.strip())
