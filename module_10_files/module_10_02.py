# with open('wrote_data.txt', 'w', encoding='utf-8') as file:
#     file.write('Привет, мир!\n')
#     file.write('Еще одна строка.\n')

# names_list = ['John Peter', 'Дмитрий Антон', 'Philipp', 'Николай', 'Eugene', 'Александр', 'Мария', 'Анастасия',
#               'Марина', 'Елизавета', 'Татьяна']
# with open('wrote_data.txt', 'w', encoding='utf-8') as file:
#     for item in names_list:
#         file.write(f'{item}\n')

with open('files/appended_data.txt', 'a', encoding='utf-8') as file:
    file.write('Привет, мир!\n')
    file.write('Еще одна строка.\n')

