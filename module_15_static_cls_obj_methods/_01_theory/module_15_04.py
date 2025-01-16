class BankAccount:
    interest_rate = 0.05

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if BankAccount.is_valid_amount(amount):
            self.balance += amount
            print(f'{self.owner} пополнил счет на {amount}. Новый баланс {self.balance}')
        else:
            print(f'Неверное значение для пополнения счета {amount}')

    def withdraw(self, amount):
        if BankAccount.is_valid_amount(amount):
            self.balance -= amount
            print(f'{self.owner} снял со счета {amount}. Новый баланс {self.balance}')
        else:
            print(f'Неверное значение для снятия со счета {amount}')

    @classmethod
    def set_interest_rate(cls, new_rate):
        cls.interest_rate = new_rate
        print(f'Процентная ставка изменена на {cls.interest_rate}')

    @staticmethod
    def is_valid_amount(amount):
        return amount > 0


account = BankAccount("Ivan", 1000)
account.deposit(500)
account.deposit(-300)
account.deposit(100)
account.withdraw(-200)
account.withdraw(500)

BankAccount.set_interest_rate(0.07)

print(BankAccount.is_valid_amount(200))
