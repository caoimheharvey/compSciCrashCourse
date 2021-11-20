# reading a file
file = open('demo_text_file.txt')
content = file.read()
print(content)
file.close()

# reading lines in a file
file = open('demo_text_file.txt')
content = file.readlines()
print(content)
file.close()

# iteratively reading a file
with open('demo_text_file.txt', 'r') as file:
    for line in file:
        print(line)

# Parsing a file
with open('demo_csv_file.txt', 'r') as file:
    for line in file:
        first_name, last_name, age = line.split(',')
        print(first_name, age)

# writing to a file
with open('demo_writing_file.txt', 'w') as file:
    file.write("Writing to an existing file")

# appending to a file
with open('demo_text_file.txt', 'a') as file:
    file.write("This is a new line")

# creating a new file
with open('new_file.txt', 'w') as file:
    file.write("This is a new file")