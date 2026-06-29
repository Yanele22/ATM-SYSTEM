from atm import *

if login():

    while True:
        print("\*=*=* ATM MENU =*=*=")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. View Transactions")
        print("5. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            check_balance()

        elif choice == "2":
            deposit()

        elif choice == "3":
            withdraw()

        elif choice == "4":
            view_transactions()

        elif choice == "5":
            print("Thank you for using the ATM.\nGoodbye!")
            break

        else:
            print("Invalid option. Please try again.")