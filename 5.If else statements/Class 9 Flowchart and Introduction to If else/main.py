# If-else
"""

Conditions are statements that are created by the programmer which
evaluates actions in the program and evaluates if it's true or false.

maths = 89
science = 91

maths>90 and science>90 -> ice cream


If-then-else statement allows conditional execution based on the
evaluation of an expression.

Flowchart:
Symbols used in flowchart.
https://images.edrawmax.com/images/knowledge/flowchart-symbols1.png

Flowchart for largest of 3 numbers.
https://i2.wp.com/www.csharp-console-examples.com/wp-content/uploads/2018/03/Screenshot_7.png?resize=614%2C1001&ssl=1

Examples of if and else:
1)
if test expression:
    body of if
else:
    body of else

2)
if test expression:
    body of if

evaluates the test expression, if it is True then the body of if is executed.
If condition is false then body of else is executed.
Indentation is used to separate the blocks.
"""

num1 = input("Enter number 1: ")
num2 = input("Enter number 2: ")

# num1 = 7
# num2 = 77
# if 7>77 -> if false

if num1 > num2:
    print("This is inside else")
    print("Num 1 is the greatest number ", num1)
    print("Will this get printed?")
else:
    print("Num2")
