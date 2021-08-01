# Datatype
"""
Data Type is the type of data stored in a variable.
Type of value stored to indicate the operations performed on a variable.
Python is a dynamically typed language
"""

age = -10 # Here age is a number (int)
print(age)
age = "Jayesh" # dynamic type
print(age)
name = "Steve" # Here name is a text (string)
print(name)
pi = -3.14 # Here pi is a decimal number (float)
print(pi)

# Numeric Data type
"""
integer 12 -12
float 3.14 -3.14 3.0 -3.0
Complex no. 4 + 5j (The value of j is sqrt(-1). So 4 + 5j is 4 + 5*sqrt(-1))
Complex will not be used frequently so its ok if you dont understand it well. 
"""

# Type function
"""
gives the type of the variable
"""
print(type(1110)) integer
print(type(-10000))
print(type(3.14))
print(type(-3.14))
print(type(3.2+1j))
print(type(-99 + 1.1j))
print(type(-3.1 - 1.1j))
print(type(3.0 - 1.0j))
print(type("Jayesh is a good teacher"))
print(type("J"))
print("Jayesh is a good teacher")
print(type('J'))
print(type('123'))
print(type("123"))
print(type(123))

"""
* Try this in Meraki app: Copy the lines 29 to 43 and observe the output.
"""

number = 10
name = "Jayesh"
print(name + 1)

"""
* Try this in Meraki app: Copy the lines 49 to 51 and observe the output.
"""

# Input
"""
-> input() - This function first takes the input from the user and then evaluates the expression,
which means Python automatically identifies whether user entered a string or a number or list.
If the input provided is not correct then either syntax error or exception is raised by python.

-> How the input function works in Python :
1.When input() function executes program flow will be stopped until the user has given an input.
2.The text or message display on the output screen to ask a user to enter input value is optional i.e. the prompt,
will be printed on the screen is optional.
3.Whatever you enter as input, input function convert it into a string. If you enter an integer value still input()
function convert it into a string. You need to explicitly convert it into an integer in your code using typecasting.

-> raw_input() - This function works in older version (like Python 2.x). This function takes exactly what is typed
from the keyboard, convert it to string and then return it to the variable in which we want to store.

-> Typing of data for the raw_input() function is terminated by enter key.
We can use raw_input() to enter numeric data also. In that case we use typecasting.
"""

myinput = input("Enter a input variable of your choice ")
print(myinput)
print(int(myinput) + 123) # int("123") + 123 -> 123 + 123 = 246
print(float(myinput) + 123) # int("123") + 123 -> 123.0 + 123 = 246.0
print(complex(myinput) + 123) # complex("123") + 123 -> 123 + 0j + 123 = 246 + 0j
print(type(myinput))
myinput = int(myinput)
print(type(myinput))


"""
Changing datatype of variable is called typecasting.
The concept of typecasting is that we convert variable or constant from one datatype to another.
This will be covered in more detail in future classes.
In the above code myinput is string and on 79 type is changed from string to int.

* Try this in Meraki app: Copy the lines 77 to 84 and observe the output.
  Try different inputs like string, integer, float or complex. 
"""

# # Exercise
# """
# What is NOT a valid data type?
# a) float
# b) decimal
# c) string
# d) complex

# What is the data type of the variable temperature?
# temperature = -1.0
# a) int
# b) float
# c) complex
# d) string

# What will be the output of the program?
# print(type(2.0j))
# a) float
# b) complex
# c) number
# d) Error
# """

print(type(0+2.0j))
print(type(2.0j))