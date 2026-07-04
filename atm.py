from account import Account

accounts = [
    Account("1001", "1234", "Yanele", 1000),
    Account("1002", "5272", "Tracey", 2500),
    Account("1003", "2222", "OwnerYaya", 5000)
]

user = None

def save_transaction(transaction):
    with open("transactions.txt", "a") as file:
        file.write(transaction + "\n")

def login():
    attempts = 3

    while attempts > 0:
        pin = input("Enter PIN: ")

        if pin == user.pin:
            print("\nLogin successful!\n")
            return True

        attempts -= 1
        print(f"Incorrect PIN. Attempts remaining: {attempts}")

    print("\nAccount locked.")
    return False

def check_balance():
   print(f"\nCurrent Balance: R{user.balance:.2f}")

def deposit():
    try:
        amount = float(input("Deposit amount: R"))

        if amount <= 0:
            print("Deposit must be greater than zero.")
            return

        user.balance += amount
        save_transaction(f"Deposited: R{amount:.2f}")

        print("Deposit successful!")

    except ValueError:
        print("Please enter numbers only.")

def withdraw():
    try:
        amount = float(input("Withdraw amount: R"))

        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
            return

        if amount > user.balance:
            print("Insufficient funds.")
            return

        user.balance -= amount
        save_transaction(f"Withdrew: R{amount:.2f}")

        print("Withdrawal successful!")

    except ValueError:
        print("Please enter numbers only.")

def view_transactions():
    print("\n=*=*= TRANSACTION HISTORY =*=*=*=")

    try:
        with open("transactions.txt", "r") as file:
            history = file.read()

            if history:
                print(history)
            else:
                print("No transactions found.")

    except FileNotFoundError:
        print("No transaction history found.")