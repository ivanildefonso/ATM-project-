#Parent Class
#attibutes 
class ATM():
    def __init__(self, name, phone, address, pin, amount = 0,  balance = 1000):
        self.name = name
        self.phone = phone
        self.address = address
        self.pin = pin
        self.amount = amount
        self.balance = balance 
        
        


    def Account_info (self):
        print("Personal Details")
        print("Name ", self.name)
        print("phone ", self.phone)
        print("address ", self.address)
        print("pin  ", self.pin)
        print("Balance ", self.balance)

    
    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Current amount balance: ", self.balance)
        

    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insuficient funds!")
            print("Your current balance is {self.balance()} only")
            print("Plase enter a lesser amount")
        else:
            self.balance = self.balance - self.amount
            print("{amount()} withdrawal successful!")
            print("Current account balance: ", self.balance)
            print()

    def check_balance(self):
        print("available balance: ", self.balance)
        print()

    
#Child Class
class User (ATM):

    def __init__(self, name, phone, address, pin, balance, amount):
        self.name = name
        self.phone = phone
        self.address = address
        self.pin = pin
        self.balance = balance
        self.amount = amount


    def Account_info (self):
        print("Personal Details")
        print("Name ", self.name)
        print("phone ", self.phone)
        print("address ", self.address)
        print("pin  ", self.pin)
        print("Balance ", self.balance)

    def deposit(self,amount):
        self.amount = int(amount)
        self.balance = int(self.balance) + int(self.amount)
        print("Account balance has been updated : $", self.balance)

    def withdraw(self, amount):
        self.amount = int(amount)

        if self.amount > self.balance:
            print("Insufficient Funds | Balance Available : $", self.balance)
        else:
            self.balance = self.balance - self.amount
            print("Account balance has been updated : $", self.balance)
    
    def check_balance (self):
        print("Account balance: $", self.balance)
