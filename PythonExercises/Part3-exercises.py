"""
Type Casting
1. Convert a float to a list.
"""
# Write code here
lol = 2.123
print(list(str(lol)))

"""
Conditionals
2. Check if the key "home" exists in the below dict.
"""
contact_details = {
    "name": "Jane Doe",
    "address": "123 Main Street, Maine",
    "phone_number": {
        "mobile": "082939482",
        "home": "12345683"
    }
}

if "home" in contact_details:
    print("Yes")
else:
    print("No")

# Write code here


"""
Loops
3. Given a dictionary with all nested values, iterate through the dictionary and output each value of the nested ones.
"""

nested_dictionary = {
    "key1": [1, 2, 3, 4, 5],
    "key2": ["val1", "val2", "val3"],
    "key3": {"sub-key1": "sub-val1", "sub-key2":"sub-val2"}
}
# Write code here
for key, values in nested_dictionary.items():
    for v in values:
        print(v)


"""
Functions
4. Define a function that returns a list of odd values from 5 to some value passed as an argument.
"""
# Write code here




"""
List Comprehensions
5. Populate a list using list comprehension with even numbers 1-100
"""
# Write code here
even_numbers = [nbr for nbr in range(100) if nbr % 2 == 0]
print(even_numbers)



