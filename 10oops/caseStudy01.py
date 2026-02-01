class BankAc:
    bank_name = "state bank"

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited. Balance : {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrwan . Balance :  {self.balance}")
        else:
            print("insufficient balance")

    def show_details(self):
        print(self.name, self.balance, BankAc.bank_name)


acc1 = BankAc("abhi", 10000)
acc1.show_details()
acc1.deposit(4000)
acc1.withdraw(7000)
acc1.show_details()
