try:
    with open(r'files/data.txt', 'r', encoding='utf-8') as file:
        content = file.read()
except FileNotFoundError:
    print('Файл не найден')
except IOError:
    print('Ошибка ввода-вывода.')
else:
    print(content)
finally:
    print("Программа завершила свою работу")
