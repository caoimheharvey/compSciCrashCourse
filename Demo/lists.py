pets = ["dog", "cat", "turtle", "elephant", "pig", "cow"]

# output the 3rd value in the list
print(pets[2])

# output the 2th value from the end
print(pets[-2])

# append a value to the list
pets.append("chicken")
print(pets)

# sort the list
pets.sort()
print(pets)

# remove the 3rd value
pets.pop(2)
print(pets)

# insert new value
pets.insert(3, "cat")
print(pets)

# remove the first instance of cat
pets.remove("cat")
print(pets)

# join the list to make a string
pet_string = ' '.join(pets)
print(pet_string)