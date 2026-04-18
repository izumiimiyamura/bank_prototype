class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.initial_balance = self.balance
        self.history = []
    
    def __str__(self):
        return f"The Account Holder is {self.name} & current balance is {self.balance}"

    @classmethod
    def create(cls):
        name = input("Name: ")
        balance = float(input("Balance: "))
        return cls(name, balance)
