def read_file_lines(filename, lines):
    lines_count = 1
    with open(fr'files\{filename}', 'r', encoding='utf-8') as file:
        for line in file:
            print(line.strip())
            if lines_count == lines:
                break
            lines_count += 1


my_filename = input('Введите имя файла: ')
my_lines = int(input('Введите количество строк: '))
read_file_lines(my_filename, my_lines)
