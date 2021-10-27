"""
ATM Simulator
---------------
Requirements:
- When the program starts present the user with the ability to enter their unique 4 digit usercode.
- If the user code exists prompt them for their 4 digit pin code - they have three tries to enter this correctly
    if it is not entered correctly the program should return back to prompting the 4 digit usercode.
- There should be a total of 4 users and all should have a balance of 500.00 to start with.
- Once the user successfully logs into the system, present them with a menu containing 5 options:
    1. Check balance
        Display the users balance back to them.
    2. Withdraw cash
        Can only withdraw amounts until 100 within the values of 10, 20, 50, 80, 100
        Check the user has available balance (cannot go into the negative), if so then allow the withdraw to occur
        After the withdraw, display the user's remaining balance to them.
    3. Deposit cash
        Add the deposited amount to the user's balance
        Display the balance back to them
    4. Change pin code
        To update their pincode they must successfully enter their current pincode once, then should enter their new
        pincode twice confirming no differences between them.
        If the new pincode is valid (between 1111 and 9999) then allow it to be set.
    5. Exit
        Logs the user out of the program and displays the log in "screen" again.

- After performing a task, display the menu again and allow for selection as many times as the user wants.
- If the user selects 5-exit and then wants to quit the program after returning to the log in "screen", the user should
have the option displayed to exit by entering the value "quit"
- Balance should be displayed in Singapore Dollars.
- At the log in screen, if another user wants to log in, they should be able to.
    Ensure the correct data displays for a given user - to avoid "data leak" issues.
- Add error handling as this program will be tested once complete.
-----
This program will only use topics previously covered in Part 1-3 of the lessons.
"""

users = {
    "1234": {
        "pin": 4321,
        "balance": 500.00
    },
    "2345": {
        "pin": 5432,
        "balance": 500.00
    },
    "3456": {
        "pin": 6543,
        "balance": 500.00
    },
    "4567": {
        "pin": 7654,
        "balance": 500.00
    },
}


def withdraw(usercode):
    withdraw_amount = int(input("Please enter the amount you wish to withdraw: "))
    if withdraw_amount not in [10, 20, 50, 80, 100]:
        print("Valid amount not entered. Returning to menu.")
        return
    current_balance = users[usercode]['balance']
    if current_balance - withdraw_amount >= 0:
        users[usercode]['balance'] = current_balance - withdraw_amount
        print(f"You have withdrawn {str(withdraw_amount)}")
    else:
        print("You do not have sufficient money to withdraw.")


def deposit(usercode):
    deposit_amount = float(input("Enter the amount you'd like to deposit: "))
    users[usercode]['balance'] += deposit_amount
    print(f"Deposit of {str(deposit_amount)} has been successful.")


def change_pin(usercode, pin):
    user_existing_pin = int(input("Please verify your existing pin: "))
    if pin == user_existing_pin:
        print("You have 3 attempts to add a new pin...")
        for i in range(3):
            new_pin = int(input("Please enter your new pin: "))
            if new_pin != pin and 1111 < new_pin < 9999:
                confirmation = int(input("Please confirm your new pin: "))
                if new_pin == confirmation:
                    users[usercode]['pin'] = new_pin
                    break
                else:
                    print("Confirmation incorrect")
            else:
                print("Pin must be different than your old pin and between 1111 and 9999.")


def display_balance(usercode):
    print(f"Your balance is S$ {str(users[usercode]['balance'])}")


def check_valid_usercode(usercode):
    if usercode not in users.keys():
        return False
    return True


def check_valid_existing_pin(usercode, pin):
    if pin == users[usercode]['pin']:
        return True
    return False


exit = False
while not exit:
    menu_selection = None
    print("\n-------------------------------------------------")
    usercode = input("Please enter your user code: ")
    if usercode == "quit":
        exit = True
        break
    if check_valid_usercode(usercode):
        correct_pin = False
        for i in range(1, 4):
            pin = int(input("Please enter your pin: "))
            if not check_valid_existing_pin(usercode, pin):
                print(f"Incorrect pin. Attempt {i}/3")
            else:
                correct_pin = True
                break
        if correct_pin:
            while menu_selection != 5:
                print("Please select an option numerically from the below:")
                print("1 - Check Balance")
                print("2 - Withdraw")
                print("3 - Deposit")
                print("4 - Change pin")
                print("5 - Exit")
                menu_selection = int(input("Please enter your selection: "))
                if menu_selection == 1:
                    display_balance(usercode)
                elif menu_selection == 2:
                    withdraw(usercode)
                    display_balance(usercode)
                elif menu_selection == 3:
                    deposit(usercode)
                    display_balance(usercode)
                elif menu_selection == 4:
                    change_pin(usercode, pin)
                elif menu_selection == 5:
                    break
                else:
                    print("Not a valid selection, try again.")
