# Checking if 1 < 2
if 1 < 2:
    print("1 is less than 2")

# checking if two strings match
string1 = "helloworld"
string2 = "HelloWorld"

if string1 == string2:
    print("The strings match")
else:
    print("The strings do not match")

# checking if the length strings do not match
if len(string1) != len(string2):
    print("The strings are not the same length")
else:
    print("The strings are the same length")

# checking if an operation has a remainder
divisor = 3
if 15 % divisor == 0:
    print("No remainder")
else:
    remainder = 15 % divisor
    print(remainder)

# elif statement
if "e" in "string":
    print("e exists")
elif "i" in "string":
    print("i exists")
else:
    print("none of the values found")

# using and
s = "string"
if "e" in s and "i" in s:
    print("Both e and i exist")
elif "a" in s and "o" in s:
    print("Both a and o exist")
else:
    print("No searched letters found in provided string")

# using or
if "e" in s or "i" in s:
    print("Either e or i exist")
elif "a" in s or "o" in s:
    print("Either a or o exist")
else:
    print("No searched letters found in provided string")

