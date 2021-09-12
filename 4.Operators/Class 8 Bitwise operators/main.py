# Bitwise operators
"""
BITWISE OPERATORS are used
for manipulating data at the bit level.
&, |, ~, ^, >>, <<
Read about the not operator and binary representations:-
https://realpython.com/python-bitwise-operators/

https://realpython.com/python-bitwise-operators/#binary-number-representations
"""


"""
binary -> base 2
0,1 -> 2 digits -> represent a binary number
decimal -> base 10
0,1,2,3,4,5,6,7,8,9 -> 10 digits -> represent a decimal number

14 -> decimal
2^3 + 2^2 + 2^1 = 8+4+2 = 14

1110

2^0 = 1 * 0 = 0
2^1 = 2 * 1 = 2
2^2 = 4 * 1 = 4
2^3 = 8 * 1 = 8 
0 + 2 + 4 + 8 = 14

21
10101
2^0 = 1 * 1 = 1
2^1 = 2 * 0 = 0
2^2 = 4 * 1 = 4
2^3 = 8 * 0 = 0
2^4 = 16 * 1 = 16

1 + 0 + 4 + 0 + 16 = 21
"""

a = 9
b = 7

"""
1001 = 1*1 + 8*1 = 9
0111 = 1*1 + 2*1 + 4*1 = 7

a | b = 1111

a & b = 0001

~a = 0110 = 6
~a = -(a+1) = -10

1 | 1 = 1
0 | 1 = 1
1 | 0 = 1
0 | 0 = 0

(a&~b) | (~a&b)
a ^ b = 1110

~a = -(1001 + 1) = -1010 = -10
-10 -> 2's complement -> 0101 + 1 -> 0110

1001_
10010
1000100

"""
print(a | b)  # or
print(a & b)  # and
print(a ^ b)  # xor
print(a << 1)  # left shift
print(a << 2)
print(a >> 1)  # right shift
print(a >> 2)
