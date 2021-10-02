# Else in for loop
str_variable = "Dummy Text"
for i in str_variable:
	print(i)
else:
	print("No characters left")

# Control statements

# continue
print("=============Continue=============")
for i in str_variable:
	if i == "m":
		continue
	print(i)

# break
print("=============Break=============")
for i in str_variable:
	if i == "m":
		break
	print(i)
print("Outside the loop")

for i in str_variable:
	if i == "t":
		break
	print(i)
else:
	print("No characters left")
print("Outside the loop")


# pass
str_variable = "Dummy Text"
print("=============Pass=============")
for i in str_variable:
	if i == "m":
		pass
	print(i)

# Nested For loop
# 0, 1, 2, 3, 4
for i in range(5):
	# i = 0
	print("i is", i)
	# 0, 1, 2, 3, 4
	for j in range(5):
		print("j is ", j)
	print("End of inner loop")
print("End of outter loop")

# Example 1
# *****
# *****
# *****
# *****
# *****
print("=============Example 1=============")
answer = ""
n = 5
for i in range(n):
	print("Line",i,"has",n,".")
	for j in range(n):
		answer += "x"
	answer += "\n"
	print("Answer till line",i,"is\n",answer)
print("outside of loop")
print(answer)

# Nested For loop
# Example 2
# ***
# ***
# ***
# ***
# ***
print("=============Example 2=============")
answer = ""
n = 10
m = 5
for i in range(n):
	print("Line",i,"has",m,"*")
	for j in range(m):
		answer += "*"
	answer += "\n"
print(answer)

# Example 3
# *
# **
# ***
# ****
# *****
print("=============Example 3=============")
answer = ""
n = 5
# 0,1,2,3,4
# i =0 -> i+1 = 1
# i=1 -> i+1 = 2
# i=2 -> i+1 = 3
for i in range(n):
	print("Line",i,"has",i+1,"*")
	# j = 0, j<3
	for j in range(i+1):
		print("j is", j)
		answer += "*"
	answer += "\n"
	print("Answer till line",i,"is\n",answer)
print("===========Outside the loop=============")
print(answer)

# Example 4
# *****
# ****
# ***
# **
# *
print("=============Example 4=============")
answer = ""
n = 5
for i in range(0,n):
	print("Line",i,"has",n-i,"*")
	for j in range(0,n-i):
		answer += "*"
	answer += "\n"
print(answer)

# Example 5
#     *
#    ***
#   *****
#  *******
# *********
print("=============Example 5=============")
answer = ""
n = 5
for i in range(0,n):
	for j in range(0,n-i-1):
		answer += " "
	print("Line",i,"has",n-i-1,"\" \" and",(2*i + 1),"*")
	for j in range(0,(2*i)+1):
		answer += "*"
	answer += "\n"
print(answer)

# Example 6
# .....
# *....
# **...
# ***..
# ****.
# *****
print("=============Example 6=============")
answer = ""
n = 5
for i in range(0,n+1):
	print("Line",i,"has",i,"*","and",n-i,".")
	for j in range(0,i):
		answer += "*"
	for j in range(0,n-i):
		answer += "."
	answer += "\n"
print(answer)

# Bonus
# *********
#  *******
#   *****
#    ***
#     *
print("=============Bonus example=============")
answer = ""
n = 5
for i in range(0,n):
	print("Line",i,"has",i,"\" \" and",2*n - 2*i - 1,"*")
	for j in range(0,i):
		answer += " "
	for j in range(0,2*n - 2*i - 1):
		answer += "*"
	answer += "\n"
print(answer)
