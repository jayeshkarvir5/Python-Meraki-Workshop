# Examples
"""
Given a list of integers, replace every element by its square
"""
example_list = [1, 2, 3, 4, 5]
index = 0
while index < len(example_list):
	print("Element at",index,"is",example_list[index])
	example_list[index] = example_list[index]*example_list[index]
	print("Square is", example_list[index])
	index += 1
print("The final list is", example_list)


"""
Given a list create 4 new lists ->
- list of positive numbers
- list of negative numbers
- list of odd numbers
- list of even numbers
"""
my_list = [-1, 10, 21, -35, 40, -111, 267, 76, -894]
pos = []
neg = []
even = []
odd = []

for element in my_list:
	if element > 0:
		pos.append(element)
	elif element < 0:
		neg.append(element)
	if element % 2 == 0:
		even.append(element)
	else:
		odd.append(element)
print("List of pos nos", pos)
print("List of neg nos", neg)
print("List of even nos", even)
print("List of odd nos", odd)

index = 0
while index < len(my_list):
	element = my_list[index]
	if element > 0:
		pos.append(element)
	elif element < 0:
		neg.append(element)
	if element % 2 == 0:
		even.append(element)
	else:
		odd.append(element)
	index += 1
print("List of pos nos", pos)
print("List of neg nos", neg)
print("List of even nos", even)
print("List of odd nos", odd)

"""
Write a program that will continuously ask user to enter names, keep adding these names to a list.
If user enters “Stop”, end the program and print the number of names entered
in the list.
"""
my_list = []
while True:
	user_input = input("enter a name")
	if user_input == "Stop":
		break
	my_list.append(user_input)
print("The final list is",my_list)

# 5 numbers
my_list = []
for index in range(5):
	user_input = int(input("Enter a number "))
	my_list.append(user_input)
print("The final list is",my_list)


"""
Create list of any type and enter few elements in the list. Take an element as user
input. Search if the element is present in list . If yes, print - element found at index .....
If no, print - element not found. 
https://www.geeksforgeeks.org/python-try-except/
"""
my_list = []
len_of_list = 6
index = 0
while index < len_of_list:
	user_input = int(input("Enter a number "))
	my_list.append(user_input)
	index += 1
print("The final list is", my_list)

element = int(input("Enter the element that you want to search"))
found = False
# len(my_list)
for index in range(len_of_list):
	if element == my_list[index]:
		found = True
		print("Element Found! At index", index)
if found == False:
	print("Element not found")



"""
List of 10 students -> find avg,max,min
"""
my_list = [-1, 10, 21, -35, 40, -111, 267, 76, -894]

# [100]
# max -> 100
# [100, 200]
# max -> 100
# 200 > 100 max ->200
# [100,200,300]
# [100] -> 100
# [100,200] -> 200
# [100,200,300] -> 300
# max -> 100
# 200 > 100
# 300 > 200
# [100,200,300,400]
# max(max(max(100,200),300),400)
# avg = sum of all elements/ no of elements

avg = my_list[0]
max = my_list[0]
min = my_list[0]

# Method 1 : Inefficient way
for element1 in my_list:
	max_bool = True
	for element2 in my_list:
		if element1 < element2:
			max_bool = False
			break
	if max_bool == True:
		answer = element1
		break
print("Max is ", answer)

# Method 2 : Inefficient but efficient than Method 1
index1 = 0
while index1 < len(my_list):
	max_bool = True
	index2 = index1 + 1
	while index2 < len(my_list):
		if my_list[index1] < my_list[index2]:
			max_bool = False
			break
		index2 += 1
	if max_bool == True:
		answer = my_list[index1]
		break
	index1 += 1

# Method 3 : Most efficient method
index = 1
while index < len(my_list):
	avg += my_list[index]
	print("Compare current element", my_list[index], "with current max", max)
	print("Compare current element", my_list[index], "with current min", min)
	if my_list[index] > max:
		max = my_list[index]
	if my_list[index] < min:
		min = my_list[index]
	index += 1

print("Max is", max)
print("Min is", min)
avg /= len(my_list)
print("Avg is",avg)

"""
Find intersection of 2 lists
"""
my_list1 = [0, 10, 100, 127, 1000, 10000, -99]
my_list2 = [0, 10, 11, 127, 1000, 10001, -99]
intersection = []

for element_1 in my_list1:
	for element_2 in my_list2:
		if element_2 == element_1:
			intersection.append(element_1)
			break
print("Intersection is", intersection)

"""
Create a list of all numbers from 1 to 20 in ascending order
Using list slicing, can you create lists of even and odd numbers from the main list?
"""
all_list = []
# unpack range
all_list.extend(range(1,21))
print(all_list)
print("Even list is",all_list[1:21:2])
print("Odd list is",all_list[0:21:2])

# KBC Question
question_list = [ "How many continents are there?",  "What is the capital of India?","NG mei kaun se course padhaya jaata hai?"]
options_list = [
	["Four", "Nine", "Seven", "Eight"],
	["Chandigarh", "Bhopal", "Chennai", "Delhi"],
	["Software Engineering", "Counseling", "Tourism", "Agriculture"]
]

print(options_list[0][2])
print(options_list[1][3])
print(options_list[2][0])

# Example
# Find 2nd largest element
list1 = [100, -1, 10, 21, -35, 40, 39, 100]
# 2nd largest
max = list1[0]
index = 1
index_of_max = 0
while index < len(list1):
	if list1[index] > max:
		index_of_max = index
		max = list1[index]
	index += 1
print("max is ",max)
print("index of max", index_of_max)

# Assumption: When 2nd largest can be equal to the largest
index = 0
max2 = list1[0]
index_of_max2 = 0
if(index_of_max == 0):
	max2 = list1[1]
	index_of_max2 = 1
	index = 2
while index < len(list1):
	if list1[index] > max2 and index != index_of_max:
		max2 = list1[index]
		index_of_max2 = index
	index += 1
print("Max 2 is ", max2)
print("index of max2", index_of_max2)

# Assumption: When 2nd largest can be equal to the largest
index = 0
max2 = list1[0]
index_of_max2 = 0
if index_of_max == 0:
	max2 = list1[1]
	index_of_max2 = 1
	index = 2
while index < len(list1):
	if list1[index] > max2 and list1[index] < max:
		max2 = list1[index]
		index_of_max2 = index
	index += 1
print("Max 2 is ", max2)
print("index of max2", index_of_max2)

# Example
# Count distinct elements in the list
# Can also be solved using Dictionary(Most efficient)
# Can also be solved using set(Same efficiency but cleaner way)
"""
Dictionary -> https://www.w3schools.com/python/python_dictionaries.asp
Set -> https://www.w3schools.com/python/python_sets.asp
"""
full_list = ['a','b','c','e','a','b']
distinct_list = []

index = 0
while index < len(full_list):
	element  = full_list[index]
	index2 = 0
	not_present = True
	while index2 < len(distinct_list):
		if element == distinct_list[index2]:
			not_present = False
			break
		index2 += 1
	if not_present:
		distinct_list.append(element)
	index += 1
print("Distinct list is", distinct_list)

index = 0
while index < len(distinct_list):
	print('Count of ',distinct_list[index],'is', full_list.count(distinct_list[index]))
	index += 1