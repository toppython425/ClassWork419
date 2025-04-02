class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Баланс не может быть отрицательным!")
        self.__balance = value

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            raise ValueError('Сумма должна быть положительной!')

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            raise ValueError("Недостаточно средств или неверная сумма!")


if __name__ == '__main__':
    account = BankAccount(100)
    account.deposit(50)
    print(account.balance)
    account.withdraw(120)
    print(account.balance)
