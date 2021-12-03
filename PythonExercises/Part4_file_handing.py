"""
1. Create a file
2. Write the following string to the file:
"Hello, this is my first time writing to a file in Python. It's very exciting!"
3. Close the file
4. Read the file you just wrote to and print the contents
5. Close the file
6. Open the file and append the following string in the next line:
"I can also append to files, I'm doing great!"
7. Close the file
8. Print the contents of the file
9. Delete the file
"""

import os

# part1
file = open("myfile.txt", 'w')
file.write("Hello, this is my first time writing to a file in Python. It's very exciting!")
file.close()

# part2
file = open("myfile.txt")
print(file.read())
file.close()

print("\n")
# part 3
file = open("myfile.txt", 'a')
file.write("\nI can also append to files, I'm doing great!")
file.close()

# part 4
print(open("myfile.txt").read())

# Part 5
os.remove("myfile.txt")