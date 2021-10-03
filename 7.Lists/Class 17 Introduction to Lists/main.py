# List
student1 = "John"
student2 = "Jenny"
student3 = "Jacob"

print(student1)
print(student2)
print(student3)

print("========Using List========")
# Defining list
"""
1. Use [ to start the list, ] to end the list
2. All the values placed inside [] will be elements of the list
3. list can be of same or different type
4. List can contain any number of elements
"""
# Ordered
# Can contain data of any type
# Access by index
# Can be nested
# Mutable
# Dynamic
# student_var = "John, Jenny, Jacob"
# print(student_var)

students_list_1 = ["John", "Jenny", "Jacob"]

students_list_2 = ["John", "Jenny", "Jacob"]

students_reverse = ["Jacob", "Jenny", "John"]

print("========Compare List========")
print(students_list_1 == students_list_2)

print(students_list_1 == students_reverse)
print(students_list_1)
int_list = [41, 72, 69, 84, 101, 1, 2, 4, 5, 6, 112]
# 0th element -> 41
# 1st element -> 72
print("========Indexing========")
print(int_list[3])
print(int_list[0])
print(int_list[1])
print(int_list[2])

print("========Negative index========")
print(int_list[-1])
print(int_list[-2])
print(int_list[-3])

# IndexError: list index out of range
# print(int_list[-100])

list2 = ["this is a string", 1, 1+1j, 1.0]

print("========Multiple data types========")

print(list2)

int_list = [1, 2, 3, 4, [5,6,7,8]]

# print("========Nested List========")
print(int_list)
print(int_list[0])
print(int_list[1])
print(int_list[2])
print(int_list[3])
print(int_list[4])
print(int_list[4][2])

print("========Mutable========")
"""
https://docs.python.org/3/library/functions.html#id

https://stackoverflow.com/questions/121396/accessing-object-memory-address

https://www.geeksforgeeks.org/id-function-python/
"""
var = 5
print(id(var))
var += 5
print(id(var))

int_list = [41, 72, 69, 84, 101, 1, 2, 4, 5, 6, 112]

print("Id before appending",id(int_list))
print(int_list)
int_list.append(10)
print(int_list)

print("Id after appending", id(int_list))

print("========Append element in List========")
# """
# https://www.w3schools.com/python/python_lists_add.asp
# """
int_list = [41, 72, 69, 84, 101, 1, 2, 4, 5, 6, 112]

int_list.append(20)

print(int_list)

# int_list[4].append(30)

int_list.insert(0,100)
int_list.insert(5,1000)

print(int_list)
int_list.insert(len(int_list)-1,-61)
print(int_list)

# 10/2 = 5
# 11/2 = int(5.5) = 5
# 16/2 = int(8) = 8
index = int(len(int_list) / 2)
if len(int_list) % 2 == 1:
	index = index + 1
int_list.insert(index, "This is a string")
print(int_list)

print("========Remove element List========")
# """
# https://www.w3schools.com/python/python_lists_remove.asp
# """
int_list.pop()
print(int_list)
int_list.pop(1)
print(int_list)
int_list.append(1000)
print("Before remove 1000")
print(int_list)
# Only first occurence is removed
int_list.remove(1000)
print("After remove 1000")
print(int_list)
int_list.clear()
print(int_list)

print("========Slicing List========")
# """
# https://www.geeksforgeeks.org/python-list-slicing/
# """
# start -> starting index
# end -> ending index(this is not included)(end - 1)
# step -> increment after each element
# start : end : step
int_list = [10,20,30,40,50,60,70]
print(int_list[3:])
print(int_list[3:-1])
print(int_list[:-2])
# 0
# 0 + step = 2
# 2 + 2 = 4
# 4 +2 = 6
print(int_list[0:-1:2])
print(len(int_list))
# 0:7:2
# 0->6
print(int_list[0:len(int_list):2])

