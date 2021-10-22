# regular for each loop with a list
names = ["sarah", "mathew", "donald", "duck", "mickey", "mouse"]
for name in names:
    print(name)

# output all values from 1-100 by 5s
for i in range(1,101, 5):
    print(i)

# reverse the above
for i in range(100, 0, -5):
    print(i)

counter = 0
while counter < 10:
    counter += 1
print(counter)

mydict = {
    'name': 'Caoimhe',
    'age': 25,
    'occupation': 'Software Engineer',
    'address': ['10', 'Gopeng street', '19-22', 'Icon', '078878', 'Singapore']
}

for key, val in mydict.items():
    print(key, val)


for value in mydict.values():
    if isinstance(value, list):
        for entry in value:
            print(entry)