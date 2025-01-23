import os


def is_file_exists(filename):
    if not os.path.exists(filename):
        with open(filename, 'w') as file:
            return f'Файл создан {filename}'
    return f'Файл {filename} уже существует'


def add_participants(filename, participant_name):
    with open(filename, 'a',  encoding='utf-8') as file:
        file.write(participant_name + '\n')


def display_participants(filename):
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            participants = file.readlines()
            if participants:  # if len(participants) > 0
                print('Список участников:')
                for participant in participants:
                    print(participant.strip())
            else:
                print('Список пуст!')
    else:
        print('Файл с участниками не найден!')
