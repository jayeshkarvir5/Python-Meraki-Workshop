# Functions
# len
my_list = [1, 3, 5, 7, 9]
print("Length of my_list is", len(my_list))

# Update
"""
https://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/Iterables.html
"""
nums = [10, 20, 30, 40, 50]
# Now the list is [1, 2, 0, 4, 5]
nums[2] = 0
# print("After index 2 is updated list is", nums)
# Error because LHS is slice notation and RHS is integer
nums[2:4] = 8

# nums[2:4] = [8,'***', 10, 11] # Now list becomes [1, 2, 8, 5]
print(nums)

print("========Append element in List========")
# """
# https://www.w3schools.com/python/python_lists_add.asp
# """
int_list = [41, 72, 69, 84, 101, 1, 2, 4, 5, 6, 112]

int_list.append(20)
print(int_list)

int_list.insert(0, 100)
print(int_list)

int_list.insert(5, 1000)
print(int_list)

int_list.insert(len(int_list), -61)
# int_list.insert(len(int_list), 111)
print(int_list)

# 10/2 = 5
# 11/2 = int(5.5) = 5
# 16/2 = int(8) = 8
print("Len of the list", len(int_list))
index = int(len(int_list) / 2)
# 15/2 = 7.5 -> int(7.5) -> 7 -> if(15%2==1) -> if(1==1) -> 7+1 = 8
if len(int_list) % 2 == 1:
    index = index + 1

int_list.insert(index, 9999)
print(int_list)

int_list.insert(index, "This is a string")
print(int_list)

print("========Remove element List========")
"""
https://www.w3schools.com/python/python_lists_remove.asp
"""
int_list = [41, 72, 69, 84, 101, 1, 2, 4, 5, 6, 112]
int_list.pop()
print(int_list)

# Index
int_list.pop(1)
print(int_list)

int_list.append(1000)
int_list.insert(0, 1000)
print("Before removing 1000")
print(int_list)

# Only first occurence is removed
int_list.remove(1000)
print("After removing 1000")
print(int_list)

int_list.clear()

print(int_list)

# del
l = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140]
# end is not included
# 5 is end
# 5-1 = 4 -> 30,40,50
del l[2:5]
print(l)

#  [10,20,60,70,80,90,100,110,120,130,140]
# 2
# 2 + step = 4
# 4 + 2 = 6
# 6 + 2 =8
# 2,4,6,8
# 2,4,6
# 60,80,100
del l[2:8:2]

print(l)
# more functions
"""
https://www.w3schools.com/python/python_ref_list.asp
"""
print("========More functions on List========")

sample_list = [10, 20, 10, 21, 34, 72, -11, 10, 10, 10]

# sample_list = ['s1', 's2', 's3']

print(max(sample_list))

print(min(sample_list))

print(sample_list.count(10))

print(sample_list.index(20))

print(sample_list.index(10))

sample_list.reverse()

print(sample_list)

sample_list.sort()

print(sample_list)

# membership

my_list = [11, 22, 33, 44, 55]

print(3 in my_list)  # False
print(33 in my_list)  # True
print(5 not in my_list)  # True
print(55 not in my_list)

# concatenation

even_list = [2, 4, 6, 8]

odd_list = [1, 3, 5, 7]

print(even_list)

print(odd_list)

all_list = even_list + odd_list

print(all_list)

odd_list.extend(even_list)

print(odd_list)

odd_list.sort()
print(odd_list)

# repetition

repeat_list = [0] * 10
print(repeat_list)

repeat_list = [0, 1] * 20
print(repeat_list)

# iteration

my_list = [20, 40, 60, 80, 100]

# element in [20, 40, 60, 80, 100]
for element in my_list:
    print(element)

# [0,1,2,..4]
# index in [0,1,2,3,4]
for index in range(len(my_list)):
    print(my_list[index])

index = 0
while index < len(my_list):
    print(my_list[index])
    index += 1

# Nested Lists

random_list = [1, 2, ['A', 'B', [8.0, 8.5]], 4, 5, ['Sunday', 'Monday', ['July', 'June']]]

print("Access 8.5--------------")
# random_list[2] = ['A', 'B', [ 8.0, 8.5 ]]
# random_list[2][2] = [8.0, 8.5]
# random_list[2][2][1]
print(random_list[2])
print(random_list[2][2])

print(random_list[2][2][1])

print("Can you replace 4 and 5 by 10 and 11------------")
random_list[2][1:2] = ['C', 'D']
print(random_list)

print("Access Monday------------")
print(random_list[len(random_list) - 1][1])

print("Access June------------")
print(random_list[5][2][1])

# Examples
# List of 10 students -> find avg,max,min

# Find intersection of 2 lists

# Create a list of all numbers from 1 to 20 in ascending order
# Using list slicing, can you create lists of even and odd numbers from the main list?