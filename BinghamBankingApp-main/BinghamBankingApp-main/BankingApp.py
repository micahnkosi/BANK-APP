class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self._balance = balance  # Encapsulated balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited {amount}. New balance: {self._balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew {amount}. New balance: {self._balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def get_balance(self):
        return self._balance

class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance=0):
        super().__init__(account_number, balance)

    def deposit(self, amount):
        if amount > 0:
            interest = amount * 0.005
            super().deposit(amount + interest)
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= 700000:
            super().withdraw(amount)
        else:
            print("Withdrawal limit exceeded. Maximum withdrawal is 700,000.")

class CurrentAccount(BankAccount):
    def __init__(self, account_number, balance=0):
        super().__init__(account_number, balance)

    # No restrictions on current account

class ChildrensAccount(BankAccount):
    def __init__(self, account_number, balance=0):
        super().__init__(account_number, balance)

    def deposit(self, amount):
        if amount > 0:
            interest = amount * 0.007
            super().deposit(amount + interest)
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        print("Withdrawals are not allowed from a Children's Account.")

class StudentAccount(BankAccount):
    def __init__(self, account_number, balance=0):
        super().__init__(account_number, balance)

    def deposit(self, amount):
        if amount <= 50000:
            super().deposit(amount)
        else:
            print("Deposit limit exceeded. Maximum deposit is 50,000.")

    def withdraw(self, amount):
        if amount <= 2000:
            super().withdraw(amount)
        else:
            print("Withdrawal limit exceeded. Maximum withdrawal is 2,000.")

# Example usage
savings = SavingsAccount('S12345', 1000)
savings.deposit(1000)  # Should include interest
savings.withdraw(500000)  # Should be allowed
savings.withdraw(800000)  # Should be disallowed due to limit

current = CurrentAccount('C12345', 5000)
current.deposit(2000)
current.withdraw(3000)

children = ChildrensAccount('CH12345', 500)
children.deposit(1000)  # Should include interest
children.withdraw(100)  # Should be disallowed

student = StudentAccount('ST12345', 2000)
student.deposit(30000)  # Should be allowed
student.deposit(60000)  # Should be disallowed
student.withdraw(1000)  # Should be allowed
student.withdraw(3000)  # Should be disallowed

