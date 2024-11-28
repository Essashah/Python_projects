class BankAccount:
    def __init__(self, account_holder, balance =0):
        """ initialize the bank account with account holders name and starting balance """
        self.account_holder = account_holder #store the name of the account holder
        self.balance = balance #store initial balance

    def deposit(self,amount): 
        #add money to the account
        if amount > 0: # check if the deposit amunt is positive
            self.balance += amount
            print(f"Deposited £{amount}. New Balance £{self.balance}")
        else:
            print("deposit amount must be positive.")
    
    def withdraw(self,amount):
        #withdraw money from the account
        if amount > self.balance: #check if there is enough money to withdraw
            print(f"Insufficient funds ! your current balance is £{self.balance}")
        elif amount > 0: #check if withdrawl amount is positive
            self.balance -= amount
            print(f"withdrew £{amount}. New balance: £{self.balance}")
        else:
            print("withdrawl amount must be positive")
    def check_balance(self):
        #display the current balance.add()
        print(f"current balance £{self.balance}")

def main():
    print("Welcome to the bank account management system")

    #create a new bank account
    name = input("enter the account holders name: ")
    acount = BankAccount(name)
    #menu for account actions
    while True:
        print("\nOptions: ")
        print("1. Deposit Money")
        print("2. Withdraw money")
        print("3. check balance")
        print("4. exit")
        try:
            choice = int(input("Choose an option (1-4): "))

            if choice == 1:
                amount = float(input("Enter the amount to deposit: "))
                acount.deposit(amount)
            elif choice == 2:
                amount = float(input("Enter the amount to withdraw: "))
                acount.withdraw(amount)
            elif choice == 3:
                acount.check_balance()
            elif choice == 4:
                print("Thank you for using the Bank Account Management System. Goodbye!")
                break
            else:
                print("Invalid option. Please choose a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Run the main function
main()
    