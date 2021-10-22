num_list = [1, 2, 3, 5, 6, 7]

print("For each value in num_list")
for num in num_list:
    print(num)

string_val = "this is a string"
for s in string_val:
    print(s)

print("\nFor every second value between 0 and 20")
for num in range(0, 20, 2):
    print(num)

for i in range(len(string_val)):
    if i + 2 < len(string_val):
        break
    print(i, string_val[i])

print("\nWhile counter is less than 5")
counter = 0
while counter < 5:
    counter += 1
    # another way to write that is:
    # counter = counter + 1
print(counter)
