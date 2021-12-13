import random, string

"""
1. Sort a dictionary by values
"""

"""
2. Sort a dictionary by key
"""

"""
3. Merge two dictionaries
"""

"""
4. Find the key with the maximum unique values
"""

"""
5. Iterate through a dictionary and add 10 to any dict value that is numeric
"""
d = {'k1': 10, 'k2': 'dsk', 'k3': 39, 'k4': 60, 'k5': '30'}

"""
6. Iterate throught the following nested list structure and convert to a dict format.
If a key has multiple values you should store all values.

Hint: Import collections and use the defaultdict module
"""
nested_list = [
    ['k1', 'v1'],
    ['k2', 'v2'],
    ['k1', 'v3'],
    ['k4', 'v4'],
    ['k2', 'v5'],
    ['k6', 'v6'],
    ['k7', 'v7'],
    ['k7', 'v8']
]

"""
The following function will be used in the next exercises to generate random data. Not to be modified.
"""


def generate_random_words(num_words=100, max_word_len=10, unique_words=False):
    word_list = []
    for i in range(num_words):
        word = ''.join(random.choices(string.ascii_lowercase, k=random.randint(5, max_word_len)))
        if unique_words and word not in word_list:
            word_list.append(word)
    return word_list


"""
7. Create a dictionary that stores the contents of a list of strings by alphabetical order. 
You should NOT use a defaultdict for this.
"""

list_of_words = generate_random_words(200, unique_words=True)
print(list_of_words)


"""
8. Reverse a dictionary's key order
"""
test_dict = {'gfg' : 4, 'is' : 2, 'best' : 5}


"""
9. Remove keys from a dictionary if they contain the substring 'aaa'
"""
dictionary = {
    'pleaaase': 3,
    'willlss': 12,
    'mariaaa': 23,
    'caan':10,
    'christmaaas':10
}
