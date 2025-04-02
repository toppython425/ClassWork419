class BankAccount:

    def __init__(self, balance, owner):
        self._balance = balance
        self._owner = owner

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Баланс не может быть отрицательным!")
        self._balance = amount

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, name):
        self._owner = name

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            raise ValueError("Пополнение не может быть отрицательным!")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
        else:
            raise ValueError("Ошибка ввода или недостаточно средств!")


if __name__ == '__main__':
    user = BankAccount(1000, "Alice")

    while True:
        user_choice = input("1 - пополнить баланс. "
                            "2 - показать сумму на счете. "
                            "0 - выход из программы: ")
        if user_choice == '0':
            exit(0)
        elif user_choice == '1':
            user_deposit = float(input("Введите сумму пополнения: "))
            try:
                user.deposit(user_deposit)
            except ValueError as ex:
                print(ex)
        elif user_choice == '2':
            print(user.balance)
        else:
            print('Ошибка ввода!')

    # # Просмотр пользователя BankAccount
    # print(user.owner)
    #
    # user.deposit(100)
    # # Просмотр баланса
    # print(user.balance)
    #
    # user.deposit(1000)
    # print(user.balance)
    #
    # user.withdraw(600)
    # print(user.balance)
    #
    # # Снятие со счета
    # user.withdraw(1200)
    # print(user.balance)
