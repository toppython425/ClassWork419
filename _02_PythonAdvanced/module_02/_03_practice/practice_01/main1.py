from utils1 import *

if __name__ == '__main__':
    print(analyse_sales(r'files\sales.csv'))
    print()
    sales_data = get_data_from_csv(r'files\sales.csv')
    print(analyse_sales_from_list(sales_data))
