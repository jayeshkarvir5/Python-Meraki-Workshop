# Control statements
# Continue
i = 0
while i<10:
	i += 1
	if i <= 5:
		continue
	print("i is", i)
print("Loop body ends on the line above")

# Break
i = 0
while i<10:
	if i == 5:
		break
	print("i is", i)
	i += 1
print("Loop body ends on the line above")

# Pass
i = 0
while i<10:
	if i==5:
		pass
	print("i is", i)
	i += 1
print("Loop body ends on the line above")

# Patterns using nested loops

# *****
# *****
# *****
# *****
# *****
i = 0
while i<5:
	j = 0
	str = ""
	while j < 5:
		str += "*"
		j += 1
	print(str)
	i += 1

# *
# **
# ***
# ****
# *****
i = 0
while i<5:
	j = 0
	str = ""
	while j <= i:
		str += "*"
		j += 1
	print(str)
	i += 1

#     *
#    ***
#   *****
#  *******
# *********
i = 0
n = 5
while i < n:
	str = ""
	j = 0
	while j < n-i-1:
		str += " "
		j += 1
	j = 0
	while j < (2 * i) + 1:
		str += "*"
		j += 1
	print(str)
	i += 1
