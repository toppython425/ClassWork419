file = open('files/data.txt', 'r', encoding='utf-8')
content = file.read()
file.close()
print(content)
print()
#
# with open('data.txt', 'r', encoding='utf-8') as file:
#     content = file.read()
# print(content)


with open('files/data.txt', 'r', encoding='utf-8') as file:
    for line in file:
        print(line.strip())

with open('files/data.txt', 'r', encoding='utf-8') as file:
    clear_content = []
    content_list = file.readlines()
    for content in content_list:
        clear_content.append(content.strip())

print(clear_content)
