import Atm_classes

def add_user(name, pin) -> Atm_classes.User:

    Newuser = Atm_classes.User(name, pin, balance = 5, amount = 3)
   
    while True:
        try:
            print ("""
                    TRANSACTION

                1. Account info 
                2. Check Balance 
                3. Deposit
                4. Withdraw
                5. Exit 
        """)
            option = int(input("Enter 1, 2, 3, 4, or 5:  "))
        except:
            print ("Error: Please enter a valid number!:  /n")
            print ("Please select: 1, 2, 3, 4,or 5 :  /n")
        else:
            if option == 1:
                Newuser.Account_info()
            elif option == 2:
                Newuser.check_balance()
            elif option == 3:
                add_money = input(">>> How much money would you like to deposit?  ")
                Newuser.deposit(add_money)

            elif option == 4:
                take_money = input(">>> How much money would you like to withdraw?  ")
                Newuser.withdraw(take_money)

            elif option == 5:
                Newuser.Account_info()
                print("Thank you, come again! ")
                break
              
       
    return Newuser



def save_users(lst_Users):
    f = open('saved_users.txt', 'w')

    for newUser in lst_Users:
        f.write(newUser.name + ',' + str(newUser.pin) + "," + str(float(newUser.balance)) + '\n')
    
    f.close()
def load_users():
    f = open("saved_users.txt", "r")
    lst_Users = []
    for line in f:
        user_data = line.split(',')

    f.close()
    return lst_Users

def main():
    print("********Welcome to Bitcoin ATM*********")

    lst_Users = load_users()

    while True:
        name = str(input('Please enter your name:  '))
        pin = int(input("Enter your pin number:  "))
       
        try:
            if pin != int(pin) and name != str(name):
                raise ValueError
            print("Name and Pin Matches")
            lst_Users.append(add_user(name, pin))
        except ValueError:
            print("Name or Password is not correct")
        else:
            continue

        for User in lst_Users:
            print(User)

        save_users(lst_Users)

if __name__ == "__main__":
    main()

