#Basic Banking Interface

#Functions for menu interface

def show_balance(balance):
#Displays current balance to two decimal places (e.g. €5.46)
    print(f"Your current balance is €{balance:.2f}")

#Prompts user to input deposit amount
def deposit():
    try:
        amount = float(input("Please enter amount to be deposited:\n"))

#Prevents user from entering a negative value
    if amount < 0:
        print("Invalid deposit amount. Please try again.")
#Prevents program crashing when entering an invalid amount
        return 0
    else: 
        return amount
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return 0


def withdraw(balance):
    try:
        amount = float(input("Enter amount you wish to withdraw:\n"))
#Prevents user from withdrawing more than the current balance
    if amount > balance:
        print("Insufficient funds. Please try again")
#Prevents program crashing when entering an invalid amount        
        return 0
#Prevents user from inputting negative withdrawal amount
    elif amount < 0:
        print("Amount cannot be less than 0. Please try again")
#Prevents program crashing when entering an invalid amount
        return 0
    else:
        return amount
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return 0


#Brings everything together under one main function
def main():
    balance = 0
    is_running = True

#Prints menu selection options while program is running
    while is_running:
        print("Welcome To Python Bank!")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

#Input to select a menu option
        choice = input("Please select an option (1-4):\n")

#Calls relevant function for selected menu option
        if choice == '1':
           show_balance(balance)
    
        elif choice == '2':
#Adds deposit amount to balance figure to create new balance
            balance += deposit()    

#Subtracts withdrawal amount from balance figure to create new balance  
        elif choice == '3':
            balance -= withdraw(balance)
    
        elif choice == '4':
            is_running = False

#Validates input and prevents incorrect inputs
        else:
            print("Invalid selection. Please try again") 

#Prints upon exiting the program via option 4
    print("Thank you for choosing Python Bank!")   

if __name__ == "__main__":
    main()

