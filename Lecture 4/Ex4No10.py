class BankAccount:
    def __init__(self, owner: str, account_number: str, balance: float):
        self.__owner = owner
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount: float):
        self.__balance += amount
        self.__service_charge()

    def withdraw(self, amount: float):
        self.__balance -= amount
        self.__service_charge()

    def __service_charge(self):
        self.__balance -= self.__balance * 0.01  # decreases 1% of the balance

    @property
    def balance(self):
        return self.__balance


# Example:
account = BankAccount("Randy Riches", "12345-6789", 1000)
account.withdraw(100)
print(account.balance)  # Output: 891.0
account.deposit(100)
print(account.balance)  # Output: 981.09
