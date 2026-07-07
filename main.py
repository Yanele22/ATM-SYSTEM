from atm import *

if login():

    while True:

        print("\n=*=*= ATM MENU =*=*=")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. View Transactions")
        print("5. Account Details")
        print("6. Change PIN")
        print("7. Logout")
        print("8. Exit")

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
            account_details()

        elif choice == "6":
            change_pin()

        elif choice == "7":
            logout()

            if login():
                continue
            else:
                break

        elif choice == "8":
            print("Thank you for using our ATM.")
            break

        else:
            print("Invalid option.")