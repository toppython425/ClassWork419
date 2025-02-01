import json


def write_data_to_json(filename, data):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(
                obj=data,
                fp=file,
                ensure_ascii=False,
                indent=4
            )
    except FileNotFoundError:
        print('Папка не найдена!')
        return

    return f'Данные записаны в: {filename}'


data_to_write = {'Name': 'Alice', 'Age': 30, 'Навыки': ['Python', 'Data Analysis']}

if __name__ == '__main__':
    result = write_data_to_json(r'files/write_example.json', data_to_write)
    print(result)
