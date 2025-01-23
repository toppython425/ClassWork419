# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self._account_number = "12345"
#         self.__balance = balance



class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._account_number = "12345"
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    # def set_balance(self, new_balance):
    #     if amount > 0:
    #         self.__balance = new_balance


if __name__ == '__main__':
    account = BankAccount("Алиса", 1000)
    print(account.get_balance())
