import os


def count_words(filename):
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            words = content.split()
            print(f'Количество слов в файле: {len(words)}')
    else:
        print('Файл не найден')


def count_lines(filename):
    lines_counter = 0
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                lines_counter += 1
            print(lines_counter)

    else:
        print('Файл не найден')

def count_lines_1(filename):
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            print(len(file.readlines()))
    else:
        print('Файл не найден')


file_name = 'files/participants.txt'
count_words(file_name)
count_lines(file_name)
count_lines_1(file_name)
