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