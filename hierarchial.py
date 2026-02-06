class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.account_holder} deposited ₹{amount}. New Balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{self.account_holder} withdrew ₹{amount}. New Balance: ₹{self.balance}")
        else:
            print("Insufficient balance!")

    def display_balance(self):
        print(f"Account Holder: {self.account_holder}, Balance: ₹{self.balance}")


class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance, interest_rate):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        print(f"Interest of ₹{interest} added. New Balance: ₹{self.balance}")


class CurrentAccount(BankAccount):
    def __init__(self, account_holder, balance, overdraft_limit):
        super().__init__(account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw_with_overdraft(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"{self.account_holder} withdrew ₹{amount} with overdraft. New Balance: ₹{self.balance}")
        else:
            print("Withdrawal exceeds overdraft limit!")
            
savings = SavingsAccount("Darshan", 10000, 5)
savings.display_balance()
savings.deposit(2000)
savings.withdraw(3000)
savings.add_interest()
savings.display_balance()

print("\n-----------------------------\n")

current = CurrentAccount("Kiran", 5000, 2000)
current.display_balance()
current.deposit(1500)
current.withdraw(4000)
current.withdraw_with_overdraft(6000)  # within overdraft limit
current.withdraw_with_overdraft(3000)  # exceeds overdraft limit
current.display_balance()
