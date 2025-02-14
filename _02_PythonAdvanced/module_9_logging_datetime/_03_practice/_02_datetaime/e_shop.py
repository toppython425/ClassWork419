from datetime import datetime, timedelta


def add_weekdays(start_date, num_days, work_days):
    """
    :param start_date: дата заказа
    :param num_days: срок доставки заказа
    :param work_days: количество рабочих дней магазина
    :return: дата доставки
    """
    current_date = start_date
    while num_days > 0:  # 5
        current_date += timedelta(days=1)
        if current_date.weekday() < work_days:
            # current_date.weekday() индекс текущего дня недели < количества рабочих дней в неделе.
            num_days -= 1
    return current_date


if __name__ == '__main__':
    date_now = datetime.now()
    print(date_now.weekday() + 1)
    delivery_date = add_weekdays(date_now, num_days=5, work_days=6)
    print(f'Дата доставки: {delivery_date.strftime('Дата: %Y-%m-%d. Время: %H:%M:%S')}')
