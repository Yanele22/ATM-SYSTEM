from account import Account


user = Account("1234", 1000)

def save_transaction(transaction):
    with open("transactions.txt", "a") as file:
        file.write(transaction + "\n")


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
        save_transaction(f"Deposited: R{amount:.2f}")
        print("Deposit successful!")
    else:
        print("Invalid amount")

def withdraw():
    amount = float(input("Withdraw amount: R"))

    if amount <= user.balance:
        user.balance -= amount
        save_transaction(f"Withdrew: R{amount:.2f}")
        print("Withdrawal successful!")
    else:
        print("Insufficient funds")

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