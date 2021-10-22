"""
Write a python program that:
1.Given a string check if it contains the letters "i" and "u" or "a"
2. If it does, divide the length of the string by 2.
    Output the result of the remainder, if its 0 then output "no remainder and contains i, u or a"
3. If it does not, divide the length of the string by 3.
    Output the result of the remainder, if its 0 then output "no remainder and does not container i, u or a"

Bonus:
4. if it does not contain i, u , a, add another condition to check if it contains "o" or "e", if it does,
    then multiply the length of the string by 5 and divide it by 2 checking for a remainder.

NOTE: Do not use loops
"""
s = "this is a string"

# Write the code here
if "i" in s and "u" in s or "a" in s:
    r = len(s) % 2
    if r == 0:
        print("No remainder and contains i, u or a")
    else:
        print(r)
elif "o" in s or "e" in s:
    r = (len(s) * 5) % 2
    if r == 0:
        print("No remainder and contains o or e")
    else:
        print(r)
else:
    r = len(s) % 3
    if r == 0:
        print("No remainder but does not contains i, u or a")
    else:
        print(r)
