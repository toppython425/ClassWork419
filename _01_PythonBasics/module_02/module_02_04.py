# number = int("hello")
# result = 10 / 0
# file = open('myfile.txt')
# my_list = [1, 2, 3, 4]
# print(my_list[5])
# result = 'text' + 5
from traceback import print_tb

try:
    result = 10 / 0
except ZeroDivisionError:
    print("На ноль делить нельзя!")

print("Исключение ZeroDivisionError отработано")
print()

try:
    number = int(input("Введите число: "))
except ValueError:
    print("Это не число!")
else:
    print(f'Вы ввели число: {number}')
print("Исключение ValueError отработано")
print()

try:
    file = open('example.txt')
    data = file.read()
except FileNotFoundError:
    print("Файл не найден!")
finally:
    try:
        file.close()
        print("Файл закрыт")
    except NameError:
        print('Переменная file не задана/объект не был создан')

print("Исключение FileNotFoundError отработано")
