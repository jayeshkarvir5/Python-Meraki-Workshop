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