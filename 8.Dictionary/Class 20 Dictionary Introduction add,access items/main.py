# Dictionary
"""
Dictionaries are used to store data values in key:value pairs.
A dictionary is a collection which is ordered, changeable and does not allow
duplicates
Dictionaries are written with curly brackets, and have keys and values

When to use Dictionary?
1.When the data has a unique reference that can be associated with the value.
2.When quick access to data items is important. Dictionaries are designed to let us find a value instantly without the need for searching through the whole collection.
3.As dictionaries are mutable, it is not a good idea to use dictionaries to store data that shouldn’t be modified in the first place.
4.When memory consideration is not an important factor for the application. Compared to lists and tuples, dictionaries take up more space in memory.
5.When the data order is not important.

Few tutorials:
https://towardsdatascience.com/python-dictionaries-651acb069f94

https://realpython.com/python-dicts/
"""

car_dict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964,
748: "Just a random number"
}

print(car_dict)

# Accessing elements
print(car_dict['brand'])
print(car_dict['model'])
print(car_dict['year'])
print(car_dict[748])

# Get method
print(car_dict.get('brand'))
print(car_dict.get('brand1'))
# Error
# print(car_dict['brand1'])

nested_dict = {'Dict1': {1: 'Geeks'}, 'Dict2': {'Name': 'For'}}

print(nested_dict['Dict1'])
print(nested_dict['Dict1'][1])

# Add/Update
"""
One value at a time can be added to a Dictionary by defining value along with
the key e.g. Dict[Key] = ‘Value’.
Or using the update method
"""

car_dict['owner'] = 'Jayesh'
print(car_dict)

"""
The update() method updates the dictionary with the elements
from the another dictionary object or from an iterable of
key/value pairs.
update() method adds element(s) to the dictionary if the key is not
in the dictionary. If the key is in the dictionary, it updates the key
with the new value.
If update() is called without passing parameters, the dictionary
remains unchanged.
"""

car_dict.update({'owner':'John'})

print(car_dict)

d = {'x': 2}

tup = ('y',3,'z',0)
print(tup)
print(tup[0])
tup = (('y',3), ('z', 0))
print(tup[0])
print(tup[0][0])
d.update(tup)

print(d)
"""
Tuples
https://www.w3schools.com/python/python_tuples.asp
"""

# Properties of keys
"""
More than one entry per key is not allowed ( no duplicate key is allowed)
The values in the dictionary can be of any type, while the keys must be immutable like numbers, tuples, or strings.
Dictionary keys are case sensitive- Same key name but with the different cases are treated as different keys in Python dictionaries.
"""
