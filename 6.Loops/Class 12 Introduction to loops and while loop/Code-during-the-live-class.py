# While loop
"""
while test_expression:
    Body of while
"""
# print numbers from 1 to 10
# print(1)
# print(2)
# print(3)
# print(4)
# print(5)
# print(6)
# print(7)
# print(8)
# print(9)
# print(10)

i = 15
while i>=1:
	print(i)
	i -= 1



# On line 18 i = 1
# On line 19, 1 <=10 -> true - >while true
# On line 20 print(i) -> 1
# On line 21 i = i +1 = 2
# Interpreter comes to line 9, 2 <= 10
# while 11 <= 10
#
# i = 100 + 1 = 101
# while 101 <= 100


# Program to add natural
# numbers up to
# sum = 1+2+3+...+n

# To take input from the user,
n = int(input("Enter n: "))
# # n = 99

sum = 0

i = 1

while i <= n:
    sum = sum + i
    i = i+1

print("i is (n+1)", i)
print("The sum is", sum)

# i = 1, n = 10 1<=10
# sum = sum + i = 0 + 1 = 1 -> sum = 1
# i = 2, n = 10 2 <= 10
# sum = 1 + 2 = 3
# i = 3, n =10, 3<=10
# sum = 3 + 3 = 6
# 4 10 4<=10
# ......
# 10 10 10<=10
# sum = 45 + 10 = 55
# i=16 16<=15

# while with else
'''
Example to illustrate
the use of else statement
with the while loop
'''

counter = 0

while counter < 3:
    print("Inside loop")
    counter = counter + 1
else:
    print("Inside else")

# Example 2

x = 111

while x <= 100:
    print(x)
    x += 1
else:
    # (111 > 100 and 111 < 110)
    # (true and false) -> false
    if 100 < x and x < 110:
        print("x is between 100 and 110")
    else:
        print("x is greater than 110")

# 98
# 99
# 100
# x is between 100 and 110


# Take a number m input from the user
# take m numbers from the user
# find the product of these m numbers and print the product


m = int(input("Enter the value of m:"))
i = 1
product = 1
while i <= m:
    my_number = int(input("Enter the value of my no:"))
    product = product * my_number
    i = i + 1
print("The product of all the numbers inputted is ", product)

# (10, 20, 30)
# 1 * 10 * 20 * 30