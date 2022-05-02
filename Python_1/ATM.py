class ATM():
    
    def __init__ (self, name, pin, balance = 1000):
        self.name = name 
        self.pin = pin
        self.balance = balance

    def account_info (self):
        print("\n Welcome to your account")
        print('Account holder: {self.name.upper()}')
        print("Account number: {self.pin()}")
        print("Available Balance: {self.balance()}")

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Current amount balance: ", self.balance)
        print()

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

    def transaction(self):
        print("""
                TRANSACTION
            1. Account Detail
            2. Check Balance 
            3. Deposit
            4. Withdraw
            5. Exit 
      """  )

        while True:
            try:
                option = int(input("Enter 1, 2, 3, 4 or 5"))
            except:
                print ("Error: Please enter a valid number!/n")
                print ('Please select: 1, 2, 3, 4, or 5')
            else:
                if option == 1:
                    ATM.account_info()
                elif option == 2:
                    ATM.check_balance()
                elif option == 3:
                    ATM.deposit()
                elif option == 4:
                    ATM.withdraw
                elif option == 5:
                    print("""
                Transaction is complete
                
            Account holder: {self.name.upper()}
            Account pin: {self.pin()}
            Available balance {self.balance()}
                
                Thank you, come again!


                  """)
            
            

        



