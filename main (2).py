class BankAccount:
    def __init__(self, account_number, account_holder_name, account_balance):

        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = account_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print(f"{amount} has been deposited to your account.")
        else:
            print("Invalid amount. Please enter a positive value.")
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            print(f"{amount} has been withdrawn from your account.")
        else:
            print("Invalid amount. Please enter a positive value that is less than or equal to your account balance.")

    def display_balance(self):
        print(f"Your account balance is {self.__account_balance:.2f}.")

my_account = BankAccount(1234567890, "John Doe", 10000)

my_account.deposit(5000)
my_account.deposit(-1000)

my_account.withdraw(3000)
my_account.withdraw(20000)

my_account.display_balance()
