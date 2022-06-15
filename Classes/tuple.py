

# We can iterate over the tuple, just like we iterate over the lists.
'''tuple_list = ('Red', 'Green', 'Blue', 'Yellow', 'Purple', 'Cyan')
items = ""
for item in tuple_list:
    items += item
    items += " "
print(items)
print(type(items))'''

# Tuple objects does not support item assignment

tuple_list = ('Red', 'Green', 'Blue', 'Yellow', 'Purple', 'Cyan')
'''items = ""
for item in range(len(tuple_list)):
    tuple_list[item] = "Changed value"
    items += " "
print(tuple_list)
print(type(tuple_list))
'''

print(tuple_list[0])
print(type(tuple_list[0]))


# Its a tuple 
a = 4,
print(type(a))
