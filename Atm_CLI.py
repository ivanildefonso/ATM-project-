from textwrap import indent
import Atm_classes
import json
from pymongo import MongoClient

def add_user(name, phone, address, pin) -> Atm_classes.User:

    client =  MongoClient() 
    atmuserdb = client.atmuserdb

    Newuser = Atm_classes.User(name, phone, address, pin, balance = 0, amount = 0)
    lst_Users = load_users()
    while True:
        try:
            print ("""
                    TRANSACTION

                1. Account info 
                2. Check Balance 
                3. Deposit
                4. Withdraw
                5. Exit (save to mongodb)
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
                save_to_db(Newuser, atmuserdb)
                save_users([Newuser])

                print("Thank you, come again! ")
                break
              
       
    return Newuser

def save_to_db(user, atmuserdb):
    dict_user = {
        "name" : user.name,
        "address" : user.address,
        "phone" : user.phone,
        "pin" : user.pin,
        "balance" : user.balance
    }
    
    atmuserdb.user.insert_one(dict_user)


    
def save_users(lst_Users):
    user_dict = {
        "name" : lst_Users[0].name,
        "address" : lst_Users[0].address,
        "phone" : lst_Users[0].phone,
        "pin" : lst_Users[0].pin,
        "balance" : lst_Users[0].balance
    
    }

    f = open('user.json', 'a')

    json.dump(user_dict, f, indent = 4, separators=(',',': '))

    f.close()


def load_users():
    f = open("user.json", "r")
    lst_Users = []
    for line in f:
        user_data = line.split(',')

    f.close()
    return lst_Users

def main():
    check_connection = True
    try:
        client = MongoClient()
        atmuserdb = client.newUser
    except BaseException:
        print("Sorry, cannot connect!")
        check_connection = False

    print("********Welcome to Bitcoin ATM*********")

    lst_Users = load_users()

    while True:
        print("Please begin with creating an account")
        name = input("Enter your name: ")
        phone = input("Enter your phone number: ")
        address = input("Enter your address: ")
        pin = input("Please enter a 4 digit pin to use as your passcode: ")

        print()
        print("Your account summary is:")
        print("Name:" + name)
        print("Phone Number:" + phone)     
        print("Address:" + address)
        print("Pin Code:" + pin)    
        print()
        print(name,", Thank you for creating an account.")

        name = str(input('Please enter your name:  '))
        pin = int(input("Enter your pin number:  "))
       
        try:
            if pin != int(pin) and name != str(name):
                raise ValueError
            print("Name and Pin Matches")
            lst_Users.append(add_user(name, phone, address, pin))
        except ValueError:
            print("Name or Password is not correct")
        else:
            continue

        for User in lst_Users:
            print(User)

        save_users(lst_Users)

if __name__ == "__main__":
    main()

