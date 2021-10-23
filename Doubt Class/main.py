# Doubt class
# Example 1
# input : - 3 x 3 square (9 numbers)
# Output :- yes if its a magic square or else no
magic_square = [
				[8,1,6],
				[3,5,7],
				[4,9,2]
				]
# magic_square = [
# 				[16,3,2,13],
# 				[5,10,11,8],
# 				[9,6,7,12],
# 				[4,15,14,1]
# 				]
# The code is generic and it can handle 4x4,5x5,...nxn square. To test it out you may uncomment the above variable.
# sum of all element in a row = sum of all elements in a column = sum of all elements in a diagonal


magic_square_boolean = True
magic_sum = 0
# diagonal 1
# (0,0), (1,1), (2,2)

sum_diag = [] # just for reference
for i in range(0,len(magic_square)):
	print(magic_square[i][i])
	magic_sum = magic_sum + magic_square[i][i]
print(magic_sum)
sum_diag.append(magic_sum)
print("==========================")

# diagonal 2
# (0,2), (1,1), (2,0)
# i = 0, (0, 3-0-1) ->(0,2)
# i = 1, (1,3-1-1) -> (1,1)
# i = 2, (2,3-2-1) -> (2,0)
sum = 0
l = len(magic_square)
for i in range(0,l):
	print(magic_square[i][l-i-1])
	sum = sum + magic_square[i][l-i-1]
print(sum)
sum_diag.append(sum)
print(sum_diag)

if magic_sum != sum:  # if any sum does not match then it is not a magic square
	magic_square_boolean = False

# row
# i in range(0,3) -> i in [0,1,2]
# j in range(0,magic_square[i]) -> j in [0,1,2]
# sum = sum + 8 + 1 + 6 = 15
# sum = sum + magic_square[1][0]
# sum = sum + 3 + 5 + 7 = 15
# sum = sum + 4 + 9 + 2 = 15
# (0,0), (0,1), (0,2)
# (1,0), (1,1), (1,2)
# (2,0), (2,1), (2,2)
print("==========================")
sum_rows = [] # just for reference
if magic_square_boolean:
	for i in range(0,len(magic_square)):
		sum = 0
		for j in range(0,len(magic_square[i])):
			print(magic_square[i][j])
			sum = sum + magic_square[i][j]
		print("Row no is", i, "sum is", sum)
		print("==========================")
		sum_rows.append(sum)
		if magic_sum != sum: # if any sum does not match then it is not a magic square
			magic_square_boolean = False
			break
	print(sum_rows)

# columns
# (0,0) + (1,0) + (2,0)
# (0,1), (1,1), (2,1)
# (0,2), (1,2), (2,2)
sum_cols = [] # just for reference
if magic_square_boolean:
	for i in range(0,len(magic_square)):
		sum = 0
		for j in range(0,len(magic_square[i])):
			print(magic_square[j][i])
			sum = sum + magic_square[j][i]
		print("Col no is", i, "sum is", sum)
		print("==========================")
		sum_cols.append(sum)
		if magic_sum != sum: # if any sum does not match then it is not a magic square
			magic_square_boolean = False
			break
	print(sum_cols)

if magic_square_boolean:
	print("This is a magic square!")
else:
	print("Not a magic square!")


# Short version of above code
is_magic_square = True
sum_diag1 = 0
length = len(magic_square)
for i in range(0,length):
	sum_diag1 += magic_square[i][i]
sum_diag2 = 0
for i in range(0,length):
	sum_col = 0
	sum_row = 0
	sum_diag2 += magic_square[i][length-i-1]
	# magic_square[i] and magic_square will have same length because the input is a square. So we can use length variable in inner loop.
	for j in range(0,length):
		sum_col += magic_square[j][i]
		sum_row += magic_square[i][j]
	if sum_diag1 != sum_col or sum_diag1 != sum_row:
		is_magic_square = False
		break
if sum_diag1 != sum_diag2:
	is_magic_square = False
if is_magic_square:
	print("This is a magic square!")
else:
	print("Not a magic square!")


# Example 2
# Find the sum of number digits in List.
# The original list is : [12, 67, 98, 34]
# List Integer Summation : [3, 13, 17, 7]

input_list = [12, 67, 98, 34]
answer = []
# 9456 -> 9456 / 10
# remainder = 6
# quotient = 945
# divisor = 10
# dividend = 9456 -> iteration 0
# dividend = quotient * divisor + remainder
# 9456 = 945 * 10 + 6
# sum += remainder
# dividend = quotient = 945 -> iteration 1
# 945 / 10 -> r= 5, q=94
# sum = 11(6+5)
# 94 / 10 -> r= 4, q=9 sum=15 -> iteration 2
# 9/10 -> r=9, q=0
for i in range(0,len(input_list)):
	dividend = input_list[i]
	sum = 0
	while dividend > 0:
		print("Dividend is", dividend)
		remainder = dividend % 10
		sum += remainder
		dividend = int(dividend / 10) # quotient
		print("Remainder is", remainder)
	print("Sum is",sum)
	print("=======================")
	answer.append(sum)
print("Answer is", answer)
