import random

class Bank:
    def __init__(self):
        self.accounts = {}
        self.loan_feature = True
        self.total_loans = 0

    def create_account(self, name, email, address, account_type):
        account_number = str(random.randint(10000, 99999))
        if account_type not in ["Savings", "Current"]:
            raise ValueError("Invalid account type. Choose 'Savings' or 'Current'.")
        account = {
            "name": name,
            "email": email,
            "address": address,
            "type": account_type,
            "balance": 0,
            "transaction_history": [],
            "loan_count": 0
        }
        self.accounts[account_number] = account
        return account_number

    def delete_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]
        else:
            raise ValueError("Account does not exist.")

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number]["balance"] += amount
            self.accounts[account_number]["transaction_history"].append(f"Deposited {amount}")
        else:
            raise ValueError("Account does not exist.")

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            if self.accounts[account_number]["balance"] >= amount:
                self.accounts[account_number]["balance"] -= amount
                self.accounts[account_number]["transaction_history"].append(f"Withdrew {amount}")
            else:
                raise ValueError("Withdrawal amount exceeded")
        else:
            raise ValueError("Account does not exist.")

    def check_balance(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]["balance"]
        else:
            raise ValueError("Account does not exist.")

    def check_transaction_history(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]["transaction_history"]
        else:
            raise ValueError("Account does not exist.")

    def take_loan(self, account_number, amount):
        if not self.loan_feature:
            raise ValueError("Loan feature is currently off.")
        if account_number in self.accounts:
            if self.accounts[account_number]["loan_count"] < 2:
                self.accounts[account_number]["balance"] += amount
                self.accounts[account_number]["loan_count"] += 1
                self.accounts[account_number]["transaction_history"].append(f"Loan taken {amount}")
                self.total_loans += amount
            else:
                raise ValueError("Loan limit reached")
        else:
            raise ValueError("Account does not exist.")

    def transfer(self, from_account, to_account, amount):
        if from_account in self.accounts:
            if to_account in self.accounts:
                if self.accounts[from_account]["balance"] >= amount:
                    self.accounts[from_account]["balance"] -= amount
                    self.accounts[to_account]["balance"] += amount
                    self.accounts[from_account]["transaction_history"].append(f"Transferred {amount} to {to_account}")
                    self.accounts[to_account]["transaction_history"].append(f"Received {amount} from {from_account}")
                else:
                    raise ValueError("Transfer amount exceeded")
            else:
                raise ValueError("Account does not exist.")
        else:
            raise ValueError("Account does not exist.")

    def total_available_balance(self):
        return sum(account["balance"] for account in self.accounts.values())

    def account_list(self):
        return list(self.accounts.keys())

    def change_loan_feature(self):
        self.loan_feature = not self.loan_feature

    def total_loan_amount(self):
        return self.total_loans

bank = Bank()

def user_menu(bank):
    while True:
        print("\nUser Menu:")
        print("1. Create an account")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Check balance")
        print("5. Check transaction history")
        print("6. Take a loan")
        print("7. Transfer money")
        print("8. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter your name: ")
            email = input("Enter your email: ")
            address = input("Enter your address: ")
            account_type = input("Enter account type (Savings/Current): ")
            account_number = bank.create_account(name, email, address, account_type)
            print(f"Account created successfully. Your account number is {account_number}.")

        elif choice == '2':
            account_number = input("Enter your account number: ")
            amount = float(input("Enter amount to deposit: "))
            bank.deposit(account_number, amount)
            print(f"{amount} deposited successfully.")

        elif choice == '3':
            account_number = input("Enter your account number: ")
            amount = float(input("Enter amount to withdraw: "))
            bank.withdraw(account_number, amount)
            print(f"{amount} withdrawn successfully.")
           
        elif choice == '4':
            account_number = input("Enter your account number: ")
            balance = bank.check_balance(account_number)
            print(f"Your current balance is {balance}.")
            
        elif choice == '5':
            account_number = input("Enter your account number: ")
            history = bank.check_transaction_history(account_number)
            print("Transaction history:")
            for transaction in history:
                 print(transaction)
            
        elif choice == '6':
            account_number = input("Enter your account number: ")
            amount = float(input("Enter loan amount: "))
            bank.take_loan(account_number, amount)
            print(f"Loan of {amount} taken successfully.")
            
        elif choice == '7':
            from_account = input("Enter your account number: ")
            to_account = input("Enter the recipient's account number: ")
            amount = float(input("Enter amount to transfer: "))
            bank.transfer(from_account, to_account, amount)
            print(f"{amount} transferred successfully.")
           
        elif choice == '8':
            break

        else:
            print("Invalid choice. Please try again.")

def admin_menu(bank):
    while True:
        print("\nAdmin Menu:")
        print("1. Create an account")
        print("2. Delete an account")
        print("3. View all accounts")
        print("4. Check total available balance")
        print("5. Check total loan amount")
        print("6. Change loan feature")
        print("7. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter account holder's name: ")
            email = input("Enter account holder's email: ")
            address = input("Enter account holder's address: ")
            account_type = input("Enter account type (Savings/Current): ")
            account_number = bank.create_account(name, email, address, account_type)
            print(f"Account created successfully. Account number is {account_number}.")

        elif choice == '2':
            account_number = input("Enter account number to delete: ")
            bank.delete_account(account_number)
            print("Account deleted successfully.")
            

        elif choice == '3':
            accounts = bank.account_list()
            print("Accounts list:")
            for acc in accounts:
                print(acc)

        elif choice == '4':
            balance = bank.total_available_balance()
            print(f"Total available balance in the bank is {balance}.")

        elif choice == '5':
            loan_amount = bank.total_loan_amount()
            print(f"Total loan amount is {loan_amount}.")

        elif choice == '6':
            bank.change_loan_feature()
            status = "on" if bank.loan_feature else "off"
            print(f"Loan feature is now {status}.")

        elif choice == '7':
            break

        else:
            print("Invalid choice. Please try again.")

def main():
    while True:
        print("\nWelcome to the Bank Management System")
        print("1. User")
        print("2. Admin")
        print("3. Exit")

        role = input("Enter your role: ")

        if role == '1':
            user_menu(bank)
        elif role == '2':
            admin_menu(bank)
        elif role == '3':
            break
        else:
            print("Invalid role. Please choose again.")

main()
