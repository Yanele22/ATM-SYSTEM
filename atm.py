from account import Account
from datetime import datetime

# Create bank accounts
accounts = [
    Account("1001", "1234", "Yanele", 1000),
    Account("1002", "5678", "John", 2500),
    Account("1003", "9999", "Sarah", 5000)
]

current_user = None


def login():
    global current_user

    account_number = input("Enter Account Number: ")
    pin = input("Enter PIN: ")

    for account in accounts:
        if account.account_number == account_number and account.pin == pin:
            current_user = account
            print(f"\nWelcome, {current_user.name}!")
            return True

    print("Invalid account number or PIN.")
    return False


def check_balance():
    print("\n==*== ACCOUNT DETAILS ==*==")
    print(f"Account Holder: {current_user.name}")
    print(f"Account Number: {current_user.account_number}")
    print(f"Current Balance: R{current_user.balance:.2f}")

def save_transaction(transaction):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("transactions.txt", "a") as file:
        file.write(
            f"{current_time} | {current_user.account_number} | {transaction}\n"
        )


def deposit():
    try:
        amount = float(input("Deposit amount: R"))

        if amount <= 0:
            print("Deposit amount must be greater than zero.")
            return

        current_user.balance += amount

        save_transaction(f"Deposited: R{amount:.2f}")

        print("Deposit successful!")

    except ValueError:
        print("Please enter a valid number.")


def withdraw():
    try:
        amount = float(input("Withdraw amount: R"))

        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
            return

        if amount > current_user.balance:
            print("Insufficient funds.")
            return

        current_user.balance -= amount

        save_transaction(f"Withdrew: R{amount:.2f}")

        print("Withdrawal successful!")

    except ValueError:
        print("Please enter a valid number.")


def view_transactions():
    print("\n==*== TRANSACTION HISTORY ==*==")

    try:
        with open("transactions.txt", "r") as file:

            found = False

            for line in file:
                if line.startswith(current_user.account_number):
                    print(line.strip())
                    found = True

            if not found:
                print("No transactions found.")

    except FileNotFoundError:
        print("No transaction history found.")

def change_pin():
    current_pin = input("Enter your current PIN: ")

    if current_pin != current_user.pin:
        print("Incorrect PIN.")
        return

    new_pin = input("Enter your new 4-digit PIN: ")
    confirm_pin = input("Confirm your new PIN: ")

    if len(new_pin) != 4 or not new_pin.isdigit():
        print("PIN must be exactly 4 digits.")
        return

    if new_pin != confirm_pin:
        print("PINs do not match.")
        return

    current_user.pin = new_pin

    print("PIN changed successfully!")

def account_details():
    print("\n==*== ACCOUNT DETAILS ==*==")
    print(f"Account Holder : {current_user.name}")
    print(f"Account Number : {current_user.account_number}")
    print(f"Balance        : R{current_user.balance:.2f}")

def logout():
    global current_user

    print(f"\nGoodbye, {current_user.name}!")

    current_user = None

def transfer_money():
    receiver = input("Enter receiver account number: ")

    account_found = None

    for account in accounts:
        if account.account_number == receiver:
            account_found = account
            break

    if account_found is None:
        print("Account not found.")
        return

    if account_found == current_user:
        print("You cannot transfer money to yourself.")
        return

    try:
        amount = float(input("Amount to transfer: R"))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        if amount > current_user.balance:
            print("Insufficient funds.")
            return

        current_user.balance -= amount
        account_found.balance += amount

        save_transaction(
            f"Transferred R{amount:.2f} to {account_found.account_number}"
        )

        print("Transfer successful!")

    except ValueError:
        print("Invalid amount.")