# x = 10
# if x > 0:
#     print(f'{x} положительное')
#
#
# x = -10
# if x > 0:
#     print(f'{x} положительное')
# else:
#     print(f'{x} неположительное')

# x = -10
# if x > 0:
#     print(f'{x} положительное')
# elif x == 0:
#     print(f'{x} равен 0')
# else:
#     print(f'{x} отрицательное')


data = "кошка"

if type(data) == str:
    print('Условие выполнено')
    print('Этот код выполнится если условие верно')
    if data == "собака":
        print(f'Это {data}')
