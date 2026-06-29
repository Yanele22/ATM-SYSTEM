from account import Account

user = Account("1234", 1000)


def login():
    pin = input("Enter PIN: ")

    if pin == user.pin:
        print("\nLogin successful!\n")
        return True
    else: 
        print("Wrong PIN!")
        return False


def check_balance():
    print(f"\nBalance: R{user.balance}")


def deposit():
    amount = float(input("Deposit amount: R"))

    if amount > 0:
        user.balance += amount
        print("Deposit successful")
    else:
        print("Invalid amount")


def withdraw():
    amount = float(input("Withdraw amount: R"))

    if amount <= user.balance:
        user.balance -= amount
        print("Withdrawal successful")
    else:
        print("Insufficient funds")