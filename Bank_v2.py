import sys

class Transactions:
    # Validates the amount given by the user.
    def validate_amount(self, amount):
        # Type checking the amount.
        if not isinstance(amount, (int,float)):
            try:
                return float(amount)
            except ValueError:
                sys.exit()

        #Checking if the amount is negative.
        if amount < 0 :
            print("Amount cannot be negative.")
            sys.exit()
        
        # If nothing wrong return amount.
        return amount

    def withdraw(self):
        amount = self.validate_amount(float(input("Amount to withdraw: ")))

        if amount > self.balance:
            print(f"Current Balance: {self.balance}")
            return "Insufficient Balance."
        
        #Updating account balance.
        self.balance -= amount
        print(f"Remaining Balance: {self.balance}")

        #Adding the transation to history.
        self.history.append({"type": "Withdraw", "amount": amount, "balance": self.balance})
        return "Transaction successful"


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
        while True:
            name = input("Name: ")
            if not name:
                continue
            break


        try:
            balance = float(input("Balance: "))
        except ValueError:
            print("Invalid balance provided.")
            sys.exit()
        return cls(name, balance)



bank_account_1 = BankAccount.create()
bank_account_1.withdraw()
