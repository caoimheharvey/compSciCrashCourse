"""
Data Types
"""

"""
Variables and Data Types
1. Print a string, integer and list stored as a variable.
"""
# Write code here
str_var = "string"
int_var = 123
list_var = [1, 2, 3, 4]

print(str_var)
print(int_var)
print(list_var)


"""
Strings
2. Using input() enter your name, age, and address. Output the string in a format that it reads like an introduction, but
only output the first 10 characters of your address.
"""
# Write code here
name = input("Enter your name: ")
age = input("Enter your age: ")
address = input("Enter your address: ")
print(f"Hi, my name is {name}, and I'm {age} years old. I live at {address[:10]}")

"""
Lists
3. Create a list that stores animal names. Append the value “unicorn” to the list and output the list.
Set the 3rd value of the list to be upper case and sort it.
Remove “unicorn” and then insert in its position a list containing mythical creatures (centaurs, unicorns, etc.).
Output the 2nd mythical creature.
"""
# Write code here
animals = ["elephant", "dog", "cat", "mouse", "horse", "zebra"]

animals.append("unicorn")
print(animals)
animals[3] = animals[3].upper()
animals.sort()
unicorn_index = animals.index("unicorn")
animals.remove("unicorn")
animals.insert(unicorn_index, ["centaurs", "cracken", "unicorn", "griffyn"])
print(animals[unicorn_index][1])


"""
Dictionaries
4. Create a dictionary called university. There should be a name field, address field and a classes field.
The classes field should store a dictionary containing the name of the class and a list of names of the students enrolled.
Get the total number of classes (at least 4 classes).
"""
# Write code here
university = {
    "name": "someUniversity",
    "address": "123 Main Street",
    "classes": {
        "english": ["sally", "harry", "mel"],
        "compsci": ["sally", "mel"],
        "chemistry": ["marie"],
        "law": ["harry", "cary", "sherry"]
    }
}

print(len(university['classes']))
