"""
Data Types
"""

"""
Variables and Data Types
1. Print a string, integer and list stored as a variable.
"""
# Write code here
# var_string = "hello"
# var_integer = 3
# var_list = [1, 2, 3]
#
# print(var_string, var_integer, var_list)



"""
Strings
2. Using input() enter your name, age, and address. Output the string in a format that it reads like an introduction, but
only output the first 10 characters of your address.
"""
# # Write code here
# name = input("What is your name?")
# age = input("What is your age?")
# address = input("What is your address?")
#
# print(f"Hi, my name is {name}, I'm {age} and I live at {address[:10]}")


"""
Lists
3. Create a list that stores animal names. Append the value “unicorn” to the list and output the list.
Set the 3rd value of the list to be upper case and sort it.
Remove “unicorn” and then insert in its position a list containing mythical creatures (centaurs, unicorns, etc.).
Output the 2nd mythical creature.
"""
# Write code here
# animal_names = ["lion", "zebra", "elephant", "giraffe", "tiger"]
# animal_names.append("unicorn")
# print(animal_names)
#
# animal_names[2] = animal_names[2].upper()
# print(animal_names)
# animal_names.sort()
# print(animal_names)
# index_unicorn = animal_names.index("unicorn")
# animal_names.remove("unicorn")
# print(index_unicorn)
# animal_names.insert(index_unicorn, ["leprechaun", "centaur"])
# print(animal_names)
# print(animal_names[index_unicorn][1])


"""
Dictionaries
4. Create a dictionary called university. There should be a name field, address field and a classes field.
The classes field should store a dictionary containing the name of the class and a list of names of the students enrolled.
Display the names of all classes.
"""
# Write code here
university = {
    'name': 'Oxford',
    'address': '10 boulevard of broken dreams',
    'classes': {
        'english': ["Alex", "Caoimhe"],
        'literature': ["Sarah", "Jeremy"],
        'geography': ["Victor"]
    }
}

print(university['classes'].keys())

