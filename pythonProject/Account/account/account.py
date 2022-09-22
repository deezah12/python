from dataclasses import dataclass, field


@dataclass()
class Account:
    name: str
    balance: int = 0

    # def __init__(self, name):
    #     self.name = name
    #     self.balance = 0

    def deposit(self, amount):
        if amount < self.balance:
            return self.balance
        self.balance += amount

    def withdraw(self, amount, pin):
        if amount > self.balance:
            return self.balance
        self.balance -= amount

    def transfer(self, amount, name, pin=None):
        self.withdraw(amount, pin)
        name.deposit(amount)
        return name.balance
