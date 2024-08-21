#Basic Banking Interface

#Functions for menu interface

def show_balance():
#Displays current balance to two decimal places (e.g. €5.46)
    print(f"Your current balance is €{balance:.2f}")

def deposit():
#Prompts user to input deposit amount
    amount = float(input("Please enter amount to be deposited: "))

#Prevents user from entering a negative value
    if amount < 0:
        print("Invalid deposit amount. Please try again.")
#Prevents program crashing when entering an invalid amount
        return 0
    else: 
        return amount

def withdraw():
    x

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
    choice = input("Please select an option (1-4): ")

#Calls relevant function for selected menu option
    if choice == '1':
        show_balance()
    elif choice == '2':
#Adds deposit to balance figure to create new balance
        balance += deposit()    
    elif choice == '3':
        withdraw()
    elif choice == '4':
        is_running = False
#Validates input and prevents incorrect inputs
    else:
        print("Invalid selection. Please try again") 

#Prints upon exiting the program via option 4
print("Thank you for choosing Python Bank!")   

