#Questions

# 1

a=5
if(a>0):
	print("a is positive")

# 2


a,b=3,2
if(a==b):
	print(" b and a are the same numbers")
elif a<b:
	print("b is greater")
else:
	print("a is greater")


# 3
"""
Write a program to check passing marks. If marks above or equal to 40 print passed,
If marks are above 90 print passed with merit and if marks below 40 print
failed.
"""
marks = int(input("Enter your marks: "))

if marks >= 40:
	print("Passed")
elif marks > 90:
	print("Passed with merit")
else:
	print("Failed")

if marks > 90:
	print("Passed with merit")
elif marks >= 40:
	print("Passed")
else:
	print("Failed")
print("This line")

# 4
"""
Write a program to check if 2 numbers are positive. If they are positive store the product of
them in the first number, and if they are not positive then store the sum of the 2 numbers in
the first number. If only one of them is positive, then print(“only one is positive”)
"""

a, b = -3,-2

if (a > 0) and (b > 0):
	a = a * b
	# a *= b
else:
	a += b  # -3 + (-2) = -5
	if (a > 0) or (b > 0):
		print("only one is positive")
print("a and b are ", a, b)
