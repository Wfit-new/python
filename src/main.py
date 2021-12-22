class Bank:
    def __init__(self):
        self.balance = 1000
    def get_balance(self):
        return self.balance
    def withdraw(self, amount):
        self.balance = self.balance - amount
        return amount
            
# now use the class
my_bank = Bank()
my_bank.withdraw(100)
balance = my_bank.get_balance()
print(balance)
my_bank.withdraw(50)
balance = my_bank.get_balance()
print(balance)