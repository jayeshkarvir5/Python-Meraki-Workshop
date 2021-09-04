"""

Reference: https://www.programiz.com/python-programming/if-elif-else#:~:text=The%20elif%20is%20short%20for,body%20of%20else%20is%20executed.
"""

# if elif else
'''In this program, 
we check if the number is positive or
negative or zero and 
display an appropriate message'''

# num = 0

# # Try these two variations as well:
# # num = 0
# # num = -4.5


# if num > 0:
# 	print("Positive number")
# elif num == 0:
# 	print("Zero")
# 	print("This line")
# else:
# 	print("Negative number")

# n1,n2,n3. Greatest?

n1 = 10
n2 = 10
n3 = 10


if (n1 > n2) and (n1 > n3):
	print(n1, " n1 is the greatest number")
elif (n2 > n3) and (n2 > n1):
	print(n2, " n2 is the greatest number")
else:
	print(n3, " n3 is the greatest number or all numbers are equal")


# Nested if else

'''In this program, we input a number
check if the number is positive or
negative or zero and display
an appropriate message
This time we use nested if statement'''

num = float(input("Enter a number: "))
# -10
if num > 0:
    print("line 1")
    print("Positive")
else:
    print("line 2")
    if num == 0:
        print("line 3")
        print("Zero")
    else:
        print("line 4")
        print("Negative")
