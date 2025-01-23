class Cart:

    def __init__(self):
        self.items = []

    def __str__(self):
        if not self.items:
            return "Корзина пуста"
        result = 'Корзина:\n'
        total = 0
        for item in self.items:
            result += f'- {item['name']}: {item['quantity']} шт. по {item['price']} руб, сумма: {item['quantity'] * item['price']}\n'
            total += item['quantity'] * item['price']
        result += f'Итого цена корзины: {total}'
        return result

    def add_item(self, name, price, quantity=1):
        # item = {}
        # item['name'] = name
        # item['price'] = price
        # item['quantity'] = quantity
        # self.items.append(item)
        self.items.append({"name": name, 'price': price, 'quantity': quantity})

    def remove_item(self, name):
        # self.items = [item for item in self.items if item['name'] != name] # тут мы пересобираем список
        # помещая туда те элементы имя которых не равно переданному в метод имени
        for item in self.items:  # тут мы удалям элемент из списка, если найдено имя которое передано в метод
            if item['name'] == name:
                self.items.remove(item)

    def __len__(self):
        return len(self.items)

    def __add__(self, other):
        new_cart = Cart()
        new_cart.items = self.items + other.items
        return new_cart


cart1 = Cart()
cart1.add_item("Apples", 50, 2)
cart1.add_item("Milk", 80, 1)
cart1.add_item("Coffe", 150, 1)
cart1.remove_item("Coffe")

cart2 = Cart()
cart2.add_item('Bread', 40, 1)

print(cart1)
print(len(cart1))
combined_cart = cart1 + cart2
print(combined_cart)
