# class Counter:
#     count = 0
#
#     def increment(self):
#         self.count += 1  # Ошибка: создаётся локальная копия count


# counter = Counter()
# counter.increment()
# print(Counter.count)  # Вывод: 0 (глобальное поле не изменилось)
# print(counter.count)

class Counter:
    count = 0

    @classmethod
    def increment(cls):
        cls.count += 1


print(Counter.count)
Counter.increment()
print(Counter.count)
