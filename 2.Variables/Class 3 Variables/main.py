# Variables
"""
A memory location that stores data.
It has a name.
Data can change.
"""

# Example for "why we should use variables?"
# a^2 = b^2 + c^2 Pythagoras theorem
import math
a = 3
b = 4
square = (a*a) + (b*b) # Store the sum of squares of 2 sides
c = math.sqrt(square) # Square root of square variable

print("square is ", square) # This will print "square is 25"
print("Trying the formula without variables: ", math.sqrt((3*3)+(4*4)))
print("Trying the formula with variable c: ", c)
print("Trying the formula with variable square: ",math.sqrt(square))

"""
Important points to note:
1. Line 17 will print "Trying the formula without variables: 5"
2. Line 18 will print "Trying the formula with variable c: 5"
3. Line 19 will print "Trying the formula with variable square: 5"
4. All the 3 lines give the same answer for pythagoras theorem because the calculation is same.
5. The use of variables in line 17 and 18 makes the approach look clean and the variables can be used in future.
    For example, if we want to print the value of hypotenuse or use it for calculating some other variable like c2
    (assume c2 stores the hypotenuse of sides c and d) then instead of calculating(math.sqrt((3*3)+(4*4))) it again 
    we can use the variable c. Like c2 = math.sqrt((c*c) + (d*d)).
6. Why we should use variables? 
-> Store complex calculations. Reuse the answer for some other task.
   This increases the productivity as we are not performing same tasks again but instead using variables.
* Try this in Meraki app: Copy the lines 10 to 19 and observe the output.
    Make changes to a and b and check if the results match or not.   
"""

"""
Change value of variable
"""
num1 = 1000
num1 = num1 + 1111
print(num1)

"""
1000
1000 + 1111
Line 43 will print 2111
* Try this in Meraki app: Copy the lines 41 to 43 and observe the output.
"""

# Naming convention
"""
Short name or a more descriptive name
Previous example: a and b were short, marks was descriptive
Rules for Python variables:
1.Must start with a letter or the underscore character (_)
2.Cannot start with a number
3.Can only contain alphanumeric characters and underscores(A-z, 0-9, and _ )
4.Case-sensitive
MARKS, marks, Marks, MaRks are all different
"""

# Example of wrong variable names
# 1marks = 10
# marks-maths = 1234
# marks maths = 1111

# Assigning variable values
# = sign is used to assign values to the variables

maths_marks_int = 123
maths_marks_float = 123.12
student_name = "Jayesh"

print(maths_marks_int)
print(maths_marks_float)
print(student_name)

"""
* Try this in Meraki app: Copy the lines 72 to 78 and observe the output.
"""

# Dynamically Typed

dynamicVar = 100
dynamicVar = "Jayesh"
print(dynamicVar)

"""
* Try this in Meraki app: Copy the lines 86 to 88 and observe the output.
"""

# Multiple assignments

num1 = num2 = num3 = 1 # example of multiple assignments
print(num1,num2,num3) # 1 1 1
print(num1 + num2 + num3) # 1 + 1 + 1 = 3
# print(num1 + "Jayesh" + num2 + num3) # (1 + Jayesh + 1 + 1) Will give error.
print(num1,num2 + num3) # 1 1+1 = 1 2


intNum, floatNum, stringVar = 1, 2.0, "Python" # example of multiple assignments
print("My variables are ", intNum , floatNum,stringVar,sep=" ** ")

"""
Separator
',' is the separator.
Default values is " ". By specifying the sep option the default value can be changed
to use any custom value like " ** " in above example.
"""


"""
* Try this in Meraki app: Copy the lines 96 to 104 and observe the output.
  Observe how multiple assignments work. Try different values for sep and observe the output.
"""

my_input = 10
print(my_input)
# Input
my_input = input("Enter a input variable of your choice ")
print(int(my_input) + 2222)

"""
Why are we using int(my_input) instead of directly using my_input? This will be answered in class 4.
* Try this in Meraki app: Copy the lines 119 to 123 and observe the output.
  Give different values for my_input and observe the output.
"""



