import csv


def get_data_from_csv(filename):
    csv_data_list = []
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            csv_data_list.append(row)
    return csv_data_list


if __name__ == '__main__':
    for item in get_data_from_csv(r'files\users_data.csv'):
        print(item)
