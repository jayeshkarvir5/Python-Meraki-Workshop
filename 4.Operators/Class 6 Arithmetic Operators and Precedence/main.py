# Operators
"""
WHAT ARE OPERATORS?
1. Operators are special symbols in Python that carry out arithmetic or
logical computation.
2. The value that the operator operates on is called the operand.
3. For example: >>> 2+3 5. Here, + is the operator that performs addition. 2
and 3 are the operands and 5 is the output of the operation.
TYPES OF OPERATORS IN PYTHON
1. Arithmetic: +, -, /, *, //, %,**
2. Comparison: ==, <,>,<=,>=,!=
3. Identity: is, is not
4. Logical: and, or, not
5. Bitwise: &,|,^,~,<<,>>
6. Assignment: =, /=, +=,-= etc.
7. Membership: in, not in
"""

# Arithmetic
a = 11
b = 5
print(a + b)
print(a - b)  # -11 - -5 = -11 + 5
print(-a + b)  # --11 + -5 = 11 -5
print(-a - b)

# 5*2 + 1 = 11
# 101 % 100 = 1 100*1 + 1 = 101


print(a % b)  # modulus
print(17 % 10)  # 10*1 + 7 = 17
print(7 % 10)  # 10*0 + 7 = 7
print(-17 % 10)  # -17 + 10 = -7 + 10 = 3 % 10 = 3
print(-21 % 10)

print(a ** b)  # Exponentiation 11^5 = 161051
print(3 ** 4)  # 3^4 = 3 * 3 * 3 * 3 = 81
a = 11
b = 5
print(10 / 2)
print(a / b)  # Division int(a/b)
print(type(str(float(int(a / b)))))
print(a // b)  # Integer divide

"""
* Try this in Meraki app: Copy the lines 20 to 44 and observe the output.
Try different values for a and b.
"""

# Operator Precedence
"""
Operator precedence affects how an expression is evaluated.
For example, x = 7 + 3 * 2; here, x is assigned 13, not 20 because operator * has
higher precedence than +, so it first multiplies 3*2 and then adds into 7.
In the next slide, operators with the highest precedence appear at the top of
the table, those with the lowest appear at the bottom.
The highest precedence operator is ‘()’.
"""
"""
Order of precedence
1. **	Exponentiation

2. ~ + -	Complement, unary plus and minus 

3. * / % //	Multiply, divide, modulo and floor division

4. + -	Addition and subtraction

5. >> <<	Right and left bitwise shift

6. &	Bitwise 'AND'

7. ^ |	Bitwise exclusive 'OR' and regular 'OR'

8. <= < > >=	Comparison operators

9. <> == !=	Equality operators

10. = %= /= //= -= += *= **=	Assignment operators

11. is is not	Identity operators

12. in not in	Membership operators

13. not or and	Logical operators
"""

a = 10
b = 5

print(a + (b * 2))
print((a + b) * 2)
print(a * 2 + b * 2)
print(a * (2 + b) * 2)
print(a + -(a + b))
print(-(a - b))
print(~1)

a = 20
b = 10
c = 15
d = 5
e = 0

e = (a + b) * c / d  # 30 * 15 / 5
print("Value of (a + b) * c / d is ", e)

e = ((a + b) * c) / d
print("Value of ((a + b) * c) / d is ", e)

e = (a + b) * (c / d)
print("Value of (a + b) * (c / d) is ", e)

e = a + (b * c) / d
print("Value of a + (b * c) / d is ", e)

"""
* Try this in Meraki app: Copy the lines 89 to 116 and observe the output.
Try different values for a, b, c, d. 
Try different operators and experiment on how the precedence changes the output.
"""