import sys
from password_creation import creation
from pass_check import password_check
while True:
    print()
    print("-----------------------------------------")
    print("1. Create a password")
    print("2. Check the complexity of a password")
    print("0. exit program")
    print("-----------------------------------------")
    print()
    user = input("Enter a number for your choice: ")
    if user == "0":
        print("Bye, we will see you next time!!!")
        sys.exit()
    elif user == "1":
        pass_len = int(input("Please enter the length of your password: "))
        print()
        password = creation(pass_len)
        print(password)
    elif user == "2":
        if password == "":
            print("There is not a password")
        else:
            password_check(password)
    else:
        print("Please enter a right choice!!")


