# Assignment operators
"""
Assignment operators are used in Python to assign values to variables.
=, +=, -=, *=, /=, %=, //=, **=
"""
print("Assignment operators")
num1 = 12
num2 = 10
num1 += num2 # num1 = num1 + num2

print(num1)
num1 -= num2
print(num1)
num1 *= num2
print(num1)
num1 /= num2
print(num1)
num1 %= num2
print(num1) # 2
num1 += num2 # num1 = num1 + num2 = 2 + num2 = 2 + 10 =12
num1 //= num2 # num1 = num1 // num2 = 12 // 10 1
print(num1)

# Comparison operators
"""
operators that compare values and return true
or false
> , < , >= , <= , === , and !==
"""
print("Comparison operators")
print(2 == 2.0)
print(5 < 6)
print(5 > 6)
print(5 <= 6)
print(6 <= 6)
print(5 >= 6)
print(5 != 6)

# Logical operators
"""
and, or , not

x or y
OR

5<6 or 6<7 = true
yes yes = yes

5>6 or 6>7
no no = no
5<6 or 6>7
yes no = yes
5>6 or 6<7
no yes = yes

maths 95
science 94
mom maths>90 and science>90 -> ice cream


x and y
AND
yes yes = yes
Yes no = no
no yes = no
no no = no

NOT
yes = no
no = yes
"""

print("Logical operators")
print(2 == 2.0 and 2 != 2.0)  # False
# true and false
print(2 == 2.0 and not(2 != 2.0))  # true and not false = true and true
print(2 == 2.0 or 2 != 2.0)

# Membership
"""
in, not in
"""
x = ["apple", "banana"]

print("Membership operators")
print("banana" in x)
print("orange" not in x)
print("apple" in x)
print("apple" not in x)

# Identity operators
"""
Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
is, is not
"""
"""
1
2  x z
3
4
5
6
7
8  y
9
10

"""
x = ["apple", "banana"]  # red coloured fruit basket
y = ["apple", "banana"]  # blue coloured fruit basket
z = x  # z is red basket

print(x is z)

# returns True because z is the same object as x

print(x is y)  # 2 == 8 / red == blue

# # returns False because x is not the same object as y, even if they have the same content

print(x == y)  # apple, banana == apple, banana

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

