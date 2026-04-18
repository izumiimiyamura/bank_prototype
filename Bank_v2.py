class Transactions:
    # Validates the amount given by the user.
    def validate_amount(self, amount):
        # Type checking the amount.
        if not isinstance(amount, (int,float)):
            try:
                return float(amount)
            except ValueError:
                return "Invalid Amount"

        #Checking if the amount is negative.
        if amount < 0 :
            return "The Amount cannot be less than zero"
        
        # If nothing wrong return amount.
        return amount

    def withdraw(self):
        amount = self.validate_amount(float(input("Amount to withdraw: ")))
        if self.balance > amount:
            self.balance -= amount
            print(f"Remaining Balance: {self.balance}")
        return "Insufficient Balance"


class BankAccount(Transactions):
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
        try:
            balance = float(input("Balance: "))
        except ValueError:
            return "Not a Valid Balance."
        return cls(name, balance)



bank_account_1 = BankAccount.create()
bank_account_1.withdraw()
