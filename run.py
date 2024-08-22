#Basic Banking Interface

# Functions for menu interface
from colorama import init, Fore, Style

init(autoreset=True)

def show_balance(balance):
    print(f"{Fore.GREEN}Your current balance is €{balance:.2f}")

def print_welcome_banner():
    print(f"{Fore.CYAN}{Style.BRIGHT}")
    print(r"""
    =====================================
    |        Welcome to Python Bank      |
    =====================================
    """)

# Prompts user to input deposit amount
def deposit():
    try:
        amount = float(input("Please enter amount to be deposited:\n"))
        if amount < 0:
            print("Invalid deposit amount. Please try again.")
            return 0
        else:
            return amount
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return 0

# Prompts user to input withdrawal amount
def withdraw(balance):
    try:
        amount = float(input("Enter amount you wish to withdraw:\n"))
        if amount > balance:
            print("Insufficient funds. Please try again.")
            return 0
        elif amount < 0:
            print("Amount cannot be less than 0. Please try again.")
            return 0
        else:
            return amount
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return 0

# Brings everything together under one main function
def main():
    balance = 0
    is_running = True

    # Prints menu selection options while program is running
    while is_running:
        print("Welcome To Python Bank!")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        # Input to select a menu option
        choice = input("Please select an option (1-4):\n")

        # Calls relevant function for selected menu option
        if choice == '1':
            show_balance(balance)
    
        elif choice == '2':
            # Adds deposit amount to balance figure to create new balance
            balance += deposit()    

        elif choice == '3':
            # Subtracts withdrawal amount from balance figure to create new balance  
            balance -= withdraw(balance)
    
        elif choice == '4':
            is_running = False

        # Validates input and prevents incorrect inputs
        else:
            print("Invalid selection. Please try again") 

    # Prints upon exiting the program via option 4
    print("Thank you for choosing Python Bank!")   

if __name__ == "__main__":
    main()

