import csv


def write_to_csv(filename, data):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)
    return f'Данные записаны в {filename}'


data_to_write = [
    ['Name', 'Age', 'City'],
    ['Alice', '30', 'New York'],
    ['Bob', '25', 'Los Angeles'],
    ['Charlie', '35', 'Chicago'],
]

if __name__ == '__main__':
    print(write_to_csv(r'files\csv_output.csv', data_to_write))
