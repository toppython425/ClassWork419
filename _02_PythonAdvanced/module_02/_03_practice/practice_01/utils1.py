import csv


# пример из методички
def analyse_sales(file_path):
    total_revenue = 0

    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            quantity = int(row['quantity'])
            price = int(row['price'])
            total_revenue += quantity * price

    return total_revenue


# пример от преподавателя
def get_data_from_csv(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data_list = list(reader)
    return data_list


def analyse_sales_from_list(data_list):
    total_revenue = 0
    for item in data_list:
        quantity = int(item['quantity'])
        price = float(item['price'])
        total_revenue += quantity * price
    return total_revenue
