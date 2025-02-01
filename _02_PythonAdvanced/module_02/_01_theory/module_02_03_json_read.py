import json


def get_data_from_json(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            python_data = json.load(fp=file)
    except FileNotFoundError:
        print('Файл не найден!')
        return

    return python_data


if __name__ == '__main__':
    my_data = get_data_from_json(r'files/example.json')
    print(type(my_data))
    print(my_data)
