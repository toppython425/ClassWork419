from _01_01_CB_RF import parse_currency_rates
from _01_02_DATABASE import init_db, save_rates_to_db


if __name__ == '__main__':
    init_db()
    rates = parse_currency_rates()
    if save_rates_to_db(rates):
        print('Данные успешно сохранены в БД')
    else:
        print('Ошибка при сохранении данных')