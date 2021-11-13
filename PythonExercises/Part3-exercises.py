"""
Type Casting
1. Convert a float to a list.
"""
# Write code here
print(list(str(123.432)))

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
# Write code here

if "home" in contact_details.keys():
    print(True)
else:
    print(False)


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
def output_every_5(end):
    odd_vals = []
    for i in range(5, end):
        if i % 2 != 0:
            odd_vals.append(i)
    return odd_vals

print(output_every_5(27))


"""
List Comprehensions
5. Populate a list using list comprehension with even numbers 1-100
"""
# Write code here
old_dict = {1:2, 3:4, 5:6, 7:8}
dict_comprehension = {k+1:v+1 for k, v in old_dict.items()}

print(dict_comprehension)

