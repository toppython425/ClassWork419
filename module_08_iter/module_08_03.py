# with open('data.txt', 'r', encoding='utf-8') as file:
#     data_list = file.readlines()
#     print('Первые 10 строк: ')
#     print(''.join(data_list[:10]))

with open('students.txt', 'r', encoding='utf-8') as file:
    studs_iterator = iter(file)
    print('Первые 10 строк: ')
    for i in range(10):
        print(next(studs_iterator).strip())
