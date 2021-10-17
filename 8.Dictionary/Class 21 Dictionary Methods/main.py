# Delete
car_dict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964,
748: "Just a random number"
}

print(car_dict)
# Raises error if key is not found
del car_dict[748]
# del car_dict[748]
print(car_dict)

car_dict.pop('year')
# el = car_dict.pop('year')
el = car_dict.pop('year', 'No key')
print(el)
print(car_dict)

# keys
for i in car_dict:
	print(i)

# values
for i in car_dict.values():
	print(i)

# key,value
for i,j in car_dict.items():
	print(i,':',j)

# built in functions
"""
https://www.w3schools.com/python/python_ref_dictionary.asp

"""
dict_1 = {
	1 : 'one',
	2 : 'two',
	3 : 'three'
}
dict_2 = dict_1.copy()
print(dict_1)
dict_1.clear()
print(dict_1)
print(dict_2)

# from_keys
list_of_keys = ['k1', 'k2', 'k3']
values = 'val'
dict_3 = dict.fromkeys(list_of_keys, values)
print(dict_3)

# pop_item
item = dict_3.popitem()
print(item)
print(dict_3)

# setdefault
dict_2.setdefault(3, 'four')
dict_2.setdefault(4, 'four')
print(dict_2)

# Exercise
"""
Write a Python program to sum all the values in a dictionary.
d = {1:35, 2:-12, 3:47, 4: -22, 5: -13}
"""
d = {1:35, 2:-12, 3:47, 4: -22, 5: -13}
sum = 0
for value in d.values():
	sum += value
print(sum)