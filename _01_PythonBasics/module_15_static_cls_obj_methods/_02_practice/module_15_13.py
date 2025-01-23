class RestaurantOrder:
    total_orders = 0
    tables = {}

    def __init__(self, table_number, order_details):
        self.table_number = table_number
        self.order_details = order_details
        RestaurantOrder.total_orders += 1
        # RestaurantOrder.tables.setdefault(table_number, []).append(order_details)
        RestaurantOrder.tables[self.table_number] = []
        RestaurantOrder.tables[self.table_number].append(order_details)

    @staticmethod
    def is_table_available(table_number):
        return len(RestaurantOrder.tables.get(table_number, [])) == 0

    @classmethod
    def get_total_orders(cls):
        return f'Всего заказов: {cls.total_orders}'

    def add_order(self):
        RestaurantOrder.tables.setdefault(self.table_number, []).append(self.order_details)


order_1 = RestaurantOrder(1, "Caesar salad")
order_2 = RestaurantOrder(2, "Pizza Margherita")
print(RestaurantOrder.is_table_available(3))
print(RestaurantOrder.is_table_available(1))
print(RestaurantOrder.get_total_orders())
