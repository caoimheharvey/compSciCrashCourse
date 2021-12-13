"""
Update the first half of the below string to be uppercase and the second half to be lower case.
"""
half_n_half = "This is a string that is half upper case and half lower case."
half_length = round(len(half_n_half)/2)
res = half_n_half[:half_length].upper() + half_n_half[half_length:].lower()
print(res)

"""
Reverse the above string (interview question by Microsoft)
"""
print(res[::-1])
# or
print(half_n_half[::-1])


"""
Find the least frequently occuring character in the above string
"""
char_occurrence = {}
for c in half_n_half.lower():
    if c not in char_occurrence.keys():
        char_occurrence[c] = 1
    else:
        char_occurrence[c] += 1

res = min(char_occurrence, key=char_occurrence.get)
print(res)


"""
Check if the following string contains any non-alphanumeric characters
"""
s = "Do I...have non alpha numeric characters?"
print(s.isalnum())

"""
Remove the non-alpha numeric characters from the above string
"""
i = 0
print(s)
while i < len(s):
    if not s[i].isalnum():
        s = s[:i] + s[i+1:]
    else:
        i += 1

print(s)

"""
Rotate a string.
Given a string, rotate it so that the first 3 characters appear in the end
"""
string = 'hellomynameiselderprice'
string = string[3:] + string[:3]
print(string)


"""
How many times do you need to rotate the above original string to obtain the result below?
"""

expected_result = 'derpricehellomynameisel'
counter = 0
while string != expected_result:
    string = string[3:] + string[:3]
    counter += 1

print(counter)

"""
Given a list of strings, remove the letter x from all of them.
"""
list_of_strings = ['itsx', 'bexginxing', 'to', 'lookx', 'xa', 'lot', 'lixke', 'chrxistxmxaxs']

for i in range(len(list_of_strings)):
    string = list_of_strings[i]
    list_of_strings[i] = ''.join([s for s in string if s != 'x'])

print(list_of_strings)

"""
Check if a substring is present in a string
"""

substr = 'needle in haystack'
main_string = 'its like finding a needle in a haystack'

print(substr in main_string)
