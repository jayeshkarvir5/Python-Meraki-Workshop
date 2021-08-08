# String
"""
Most programming languages have a data type called a string, which is used
for data values that are made up of ordered sequences of characters, such as
"hello world". A string can contain any sequence of characters, visible or
invisible, and characters may be repeated.
Eg- “Hello”, “Chocolate”, “Animals”,”$&%@*”
In Python a string is a collection of one or more characters put in a single
quote, double-quote or triple quote. In python there is no character data type,
a character is a string of length one. It is represented by str class.

Refer w3schools for string functions.
* Try this: Open the link below and read more about string functions. Try this functions in w3school's compiler.
https://www.w3schools.com/python/python_ref_string.asp
"""

"""
Indexes in string
jaYEsh
012345
-6-5-4-3-2-1
"""
firstName = "JaYEsh"
lastName = "Karvir"
threeQuotesString = """This is a 3 quotes string """
singleQuoteString = 'This is a single quote string'
example = "123"
print(threeQuotesString)
print(singleQuoteString)


# concatenate
"""
combining 2 strings
a = "jayesh" b = "karvir"
concat -> a + b = jayeshkarvir
"jayesh" + 3 = 
1 + 3 = 4
"""
print(firstName)
print(lastName)
print(1+2)
print(firstName + " " + lastName + " this got added")
# print(firstName + 3) This will give error because string and int cannot be added or concatenated.
print("1" + "3")
print(1 + 3)
print("1.0" + "3.0")
print('1'+'3')
print("""1""" + """3""")

print(len(firstName))
# print(len(20.0)) len only takes string argument thats why this line will give error
print(firstName[-1])
print(firstName[-5])
print(firstName[-6])
print(firstName[len(firstName)-1])  # firstName[6-1=5]
print(firstName.count("j"))
print(firstName.find("x"))
print(firstName.find("t"))
print(firstName.find("J"))
print(firstName.find("s"))
print(firstName.upper())
print(firstName.casefold())
print(firstName)
firstName = firstName.upper()
firstName = firstName.casefold()
print(firstName)

"""
* Try this in Meraki app: Copy the lines 23 to 67 and observe the output.
"""

# Boolean
"""
Example: True / False

The Python Boolean type is one of Python's built-in data types. It's used to
represent the truth value of an expression. For example, the expression 1 < 2
is True , while the expression 0 == 1 is False . Understanding how Python
Boolean values behave is important to programming well in Python.
"""

isMyAgeLessThan20 = True
isMyAgeGreaterThan20 = False

"""
Comparison operators which give boolean output.
"""

print(isMyAgeGreaterThan20)
print(isMyAgeLessThan20)
print(isMyAgeLessThan20 == isMyAgeGreaterThan20)
print("jay" == "jay")
print(5 < 6)
print(5 > 6)
print(5 <= 6)
print(6 <= 6)
print(5 >= 6)
print(5 == 6)
print(5 != 6)  # not equal to

"""
* Try this in Meraki app: Copy the lines 83 to 100 and observe the output.  
"""

# # Type Casting

"""
Converting from data type to another.
"""

print(str(20) + str(20))
print(str(20) + str(30))
print(str(20)+20)  # "20" + 20
print(str(20)+"20")  # "20" + "20"
print(int("20") + int("20"))  # 20 + 20 =40
print(float("20") + float("20"))  # 20.0 + 20.0
print(int(20.2) + int(20.8))  # 20 + 20
print(20.2+20.8)
print(int(20.2+20.8))
print(int(20.2) + 20.8)

print(bool(20))
print(bool(-1))
print(bool(0))
print(bool(0.00000))
print(bool(0.000001))
# print(int("xyz")) this will give error because xyz cannot be converted to integer
print(bool("jayesh"))
print(bool(""))
print(bool(None))

"""
* Try this in Meraki app: Copy the lines 112 to 131 and observe the output.
"""