# Basic Banking Interface

# Import necessary libraries
from colorama import init, Fore, Style
import time

# Initialize colorama
init(autoreset=True)

# Function to display a welcome banner with ASCII art
def show_balance(balance):
    print(f"{Fore.GREEN}Your current balance is €{balance:.2f}")

def print_welcome_banner():
    print(f"{Fore.CYAN}{Style.BRIGHT}")
    print(r"""
    =====================================
    |        Welcome to Python Bank      |
    =====================================
    """)

# Function to display the current balance
def show_balance(balance):
    print(f"{Fore.GREEN}Your current balance is €{balance:.2f}")

# Function to handle deposits
def deposit():
    try:
        amount = float(input("Please enter amount to be deposited:\n"))
        if amount < 0:
            print(f"{Fore.RED}Invalid deposit amount. Please try again.")
            return 0
        else:
            print(f"{Fore.GREEN}Processing your deposit...")
            # Simulate processing time
            time.sleep(1)  
            print(f"{Fore.GREEN}Deposit successful!")
            return amount
    except ValueError:
        print(f"{Fore.RED}Invalid input. Please enter a valid number.")
        return 0

# Function to handle withdrawals
def withdraw(balance):
    try:
        amount = float(input("Enter amount you wish to withdraw:\n"))
        if amount > balance:
            print(f"{Fore.RED}Insufficient funds. Please try again.")
            return 0
        elif amount < 0:
            print(f"{Fore.RED}Amount cannot be less than 0. Please try again.")
            return 0
        else:
            print(f"{Fore.GREEN}Processing your withdrawal...")
            # Simulate processing time
            time.sleep(1)  
            print(f"{Fore.GREEN}Withdrawal successful!")
            return amount
    except ValueError:
        print(f"{Fore.RED}Invalid input. Please enter a valid number.")
        return 0

# Function to print a divider between sections
def print_divider():
    print(f"{Fore.BLUE}----------------------------------------")


# Main function to bring everything together
def main():
    balance = 0
    is_running = True

    print_welcome_banner()

    while is_running:
        print(f"{Fore.YELLOW}{Style.BRIGHT}\nMenu Options:")
        print(f"{Fore.CYAN}1. Show Balance")
        print(f"{Fore.CYAN}2. Deposit")
        print(f"{Fore.CYAN}3. Withdraw")
        print(f"{Fore.CYAN}4. Exit")

        # Input to select a menu option
        choice = input(f"{Fore.YELLOW}Please select an option (1-4):\n")

        # Calls relevant function for selected menu option
        if choice == '1':
            print_divider()
            show_balance(balance)
        elif choice == '2':
            print_divider()
            balance += deposit()
        elif choice == '3':
            print_divider()
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print(f"{Fore.RED}Invalid selection. Please try again.")

    print_divider()
    print(f"{Fore.GREEN}Thank you for choosing Python Bank!")

if __name__ == "__main__":
    main()

