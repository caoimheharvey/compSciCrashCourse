"""
1. Swap the first 5 elements of the list with the last 5 elements of the list
so that 20 is swapped with 60,
30 is with 43,
40 is with 12
etc.
"""
e1_list = [20, 30, 40, 10, 50, 30, 59, 43, 50, 43, 34, 40, 54, 23, 12, 43, 60]
# write code here
for i in range(5):
    start = e1_list[i]
    end = e1_list[-(i+1)]
    e1_list[i] = end
    e1_list[-(i+1)] = start
print(e1_list)

"""
2. Reverse the list in exercise 1
"""
# write code here
print(list(reversed(e1_list)))

"""
3. Output only the largest two numbers in the original list from exercise 1
"""
# write code here
sorted_list = sorted(e1_list, reverse=True)
print(sorted_list[:2])

"""
4. Output only the smallest two numbers in the original list from exercise 1
"""
# write code here
print(sorted_list[-2:])


"""
5. Count the occurrence of a user inputted value in the list from exercise 1
"""
import random
# write code here
try:
    user_input = int(input("Enter a number: "))
except ValueError:
    print("Integer not added...")
    user_input = random.randint(0, 100)

print(e1_list.count(user_input))

"""
6. Count all unique values in the list from exercise 1
"""
# write code here
unique = []
for item in e1_list:
    if e1_list.count(item) == 0:
        unique.append(item)
print(unique)

"""
7. Check if a list contains three consecutive common numbers and output which they are.
Example, in list [1,1,1,4,3,2,4,5,5,5]
The result should be 1 and 5 as three consecutive common numbers
"""
e7_list = [4, 5, 6, 7, 7, 7, 5, 4, 4, 3, 3, 3, 3, 12, 21, 12, 2, 2, 12, 12, 12, 32, 32, 43, 54, 5, 4, 44, 4, 44, 45, 6,
           7, 55, 55, 55]
# write code here
consecutive = []
for i in range(len(e7_list) - 2):
    subset = e7_list[i:i+3]
    if subset[0] == subset[1] == subset[2]:
        consecutive.append(subset[0])

print(consecutive)