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

credentials = {'0000': {'pin': '1111', 'balance': 500.00}, '1111': {'pin': '1111', 'balance': 500.00},
               '2222': {'pin': '1111', 'balance': 500.00}, '3333': {'pin': '1111', 'balance': 500.00}}


def login():
    print("Welcome to GiveUsUrMoney Bank, the most trustworthy bank in the country!")
    print("Please type your user code to enter your account, or 'exit' to terminate the session")
    bool = True

    while bool == True:
        user_code = input()
        if user_code != "exit":
            login_counter = 3
            while user_code in credentials and login_counter > 0:
                # while login_counter > 1:
                print("Please type the PIN code associated to your account")
                user_pincode = input()
                if user_pincode == credentials[user_code].get('pin'):
                    print("Welcome to your account!")
                    user_code = main_menu(user_code)
                else:
                    login_counter = login_counter - 1
                    print("Wrong PIN code, number of try remaining: " + str(login_counter))
            else:
                if login_counter < 1:
                    print("Number of try expired. Please type your user code to enter your account again")
                elif user_code == "exit":
                    print("Returning to login menu. Please type your user code to enter your account, or 'exit' to terminate the session")
                else:
                    print("We were not able to find your account, please type your PIN code again")
        else:
            print("Thank you for banking with us today!")
            bool = False


def main_menu(user_code):
    main_menu_bool = True
    while main_menu_bool == True:
        print(
            "Please select your option: \n 1. Check balance \n 2. Withdraw cash \n 3. Deposit cash \n 4. Change PIN code \n 5. Exit")
        main_menu_input = input()
        if main_menu_input == '1':
            print("You currently have " + str(credentials[user_code].get('balance')) + "SGD in your balance")
        elif main_menu_input == '2':
            print("Select the amount you want to withdraw: \n 1. 10 \n 2. 20 \n 3. 50 \n 4. 80 \n 5. 100")
            withdraw_input = input()
            withdraw_amount = 0
            if withdraw_input == '1':
                withdraw_amount = 10
            elif withdraw_input == '2':
                withdraw_amount = 20
            elif withdraw_input == '3':
                withdraw_amount = 50
            elif withdraw_input == '4':
                withdraw_amount = 80
            elif withdraw_input == '5':
                withdraw_amount = 100
            else:
                print("Please input your option choice as 1-5")
            if withdraw_amount == 0:
                continue
            elif credentials[user_code].get('balance') >= withdraw_amount:
                credentials[user_code]['balance'] -= withdraw_amount
                print("New balance: " + str(credentials[user_code]['balance']))
            else:
                print("Your balance is lower than the requested withdraw amount")
        elif main_menu_input == '3':
            print("Please input the amount you wish to deposit")
            deposit_input = float(input())
            credentials[user_code]['balance'] += deposit_input
            print("New balance: " + str(credentials[user_code]['balance']))
        elif main_menu_input == '4':
            print("Please type your current PIN code")
            menu_old_pincode = input()
            if menu_old_pincode == credentials[user_code].get('pin'):
                print("Please input your new PIN code")
                menu_new_pincode = input()
                print("Please confirm your new PIN code")
                menu_new_pincode_2 = input()
                if menu_new_pincode == menu_new_pincode_2:
                    if len(menu_new_pincode) == 4 and menu_new_pincode.isnumeric() == True and '0' not in menu_new_pincode:
                        credentials[user_code]['pin'] = menu_new_pincode
                        print(credentials[user_code].get('pin'))
                        print("Your PIN code has been successfully updated!")
                    else:
                        print("PIN code should be 4 digits only, comprised between 1 and 9. Please try again")
                else:
                    print("The PIN codes your input are different, please try again")
            else:
                print("Wrong PIN code")
                continue
        elif main_menu_input == '5':
            print("Thank you for banking with us today!")
            return "exit"
        else:
            print("Please input your option choice as 1-5")


login()
