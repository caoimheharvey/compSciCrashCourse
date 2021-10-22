transaction = {
    "amount": -5.00,
    "card_number": ["xxxx", "xxxx", "xxxx", "1234"],
    "name": "Jane Doe"
}

# output card number on transaction
card_no = transaction.get("card_number")
print(card_no)

card_no = transaction['card_number']
print(card_no)

# add field to transaction
transaction['description'] = "Water from 7/11"
print(transaction)

# delete a field
transaction.pop('description')
print(transaction)

# get all keys
keys = transaction.keys()
print(keys)

# get all values
values = transaction.values()
print(values)

# print a joined list in the dictionary
card_no_string = '-'.join(transaction['card_number'])
print(card_no_string)

# last 4 digits of card number
card_number_list = transaction['card_number']
last_four = transaction['card_number'][len(card_number_list)-1]
print(last_four)