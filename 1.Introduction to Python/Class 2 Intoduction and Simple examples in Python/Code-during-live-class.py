# Comments
# Statements followed by # are called Comments

# Error/Bugs
# The mistakes we make like syntax error or indentation error, etc

# Debug
# To solve the error/bugs

'''
Multiline Comments
dummy text
dummy text
'''

"""
This is also Multiline Comments
dummy text
dummy text
"""


# Interpreter example
"""
It checks the code line by line and the line at which
error is present, interpreter stops the code at that
line and shows the name of error. Interpreter converts
high level language to low level language with the help
of which the computer is able to run the code.
print("jayes" This error is not throw by
"""

name = "jayesh"
# Try this out in meraki app: print (name The interpreter will throw error on this line if we uncomment this because of the syntax error
print (name)

# Compiler
"""
Compiler is a software that scans the complete code in
one go and if the code contains any error ,then it
shows the error at the end of the code. Whereas the
interpreter, stops the code at the line that contains error.
Compiler is used in C and C++ programming languages.
"""

# Case sensitive

varR_jay = "amit"
vaR_jay = "jayesh123"
print (vaR_jay)
vaR_jay = "jayesh"
print (vaR_jay)

"""
print (var_jay) The interpreter will throw error on this line if we uncomment this, because var_jay does not exists.
vaR_jay exists so it gets printed.
The case (capital/small) should be exact to the variable name.
var_jay, vaR__jay, vaR_jaY, ... are some examples that have incorrect case when compared to vaR_jay

Try this out in meraki app: Copy lines 48 to 52 in meraki app, make changes in case as you like and see the output.
"""

# Indentation
"""
Wrong indentation and interpreter will throw error because the next line after if,while has no indentation

a = 10
if a * 2 == 20:
print ("this worked")
else:
print ("Variable a when mutiplied by 2 does not give 20.")

Try this out in meraki app: Copy lines 67 to 71 in meraki app and see the output.
"""

"""
Right indentation and better readability. The line after if and else have indentation.

a = 10
if a * 2 == 20:
 print ("this worked")
else:
 print ("Variable a when mutiplied by 2 does not give 20.")
  
Try this out in meraki app: Copy lines 79 to 83 in meraki app and see the output.
  
  

counter = 1
while counter < 10:
 print ("The counter is" + str(counter))
 counter = counter + 1
 print ('--------')

Try this out in meraki app: Copy lines 89 to 93 in meraki app and see the output.

counter = 1
while counter < 10:
 print ("The counter is" + str(counter))
 counter = counter + 1
print ('--------')

Try this out in meraki app: Copy lines 97 to 101 in meraki app and see the output.
"""





# Block of code
"""
It is fine to not know if or while concept.
After the concepts of if and loops are taught in future classes, your doubts will get solved.
It is ok if this concept is not clear now.
3 important things to remember.
1. Changing indentation can throw errors.
2. Changing indentation can change the output of program without throwing errors.
3. Indentation is important to get the desired output from a program.
"""

"""
In this example,

counter = 1
if counter > 1:
 counter = 2
 counter = 3
 counter = 4
 print(counter)
while counter < 10:
 counter = counter + 1
 print (counter)

Lines 126 to 129 are in same block of 'if'. Block 1
Lines 131,132 are in same block of 'while'. Block 2
Lines 124 to 132 is the entire block of code. Block 3
Try this out in meraki app: Copy from line 124 to 132 in meraki app and look at the output.
"""

"""
In this example,

counter = 1
if counter > 0:
 counter = 10
 counter = 2
 counter = 3
 counter = 4
 print(counter)
while counter < 10:
 counter = counter + 1
print (counter)

Lines 145 to 149 are in same block of 'if'. Block 1
Lines 151 is in same block of 'while'. Block 2
Lines 143 to 152 is the entire block of code. Block 3
Try this out in meraki app: Copy from line 143 to 152 in meraki app and look at the output.
"""

"""
In this example,

counter = 1
if counter > 0:
 counter = 10
 counter = 2
 counter = 3
 counter = 4
 print(counter)
 while counter < 10:
  counter = counter + 1
  print (counter)

Lines 165 to 169 are in same block of 'if'. Block 1
Lines 171 and 172 are in same block of 'while'. Block 2
Lines 163 to 172 is the entire block of code. Block 3
Try this out in meraki app: Copy from line 163 to 172 in meraki app and look at the output.
"""

