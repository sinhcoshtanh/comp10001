"""
Hello Word!
"""

print("Hola World!")
print("How are you?")

"""
Python as a calculator

Write a program that calculates and prints the factorial of  
10.
"""

print( 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2)

"""
Order of operations

Write a program that calculates and prints the results of the following two
equations:
- 5 x (8 + 20 - 18) / 2
- 5 x (8 + 20)- 18 / 2
"""

print( (5 * (8 + 20 - 18) ) / 2)
print( 5 * (8 + 20) - (18 / 2) )

"""
Musical notes

or this exercise, write a program which prints a string of notes like the one
above. Your string must start with CEGCEG followed by 36 E notes then finish
with 24 C notes.
"""

print( 'CEGCEG' + 'E' * 36 + 'C' * 24)

"""
Input exercise

Write a program that asks a user to enter their name, then prints a greeting 
for the user like this:

Enter your name: Kim
Hello Kim
"""

name = input('Enter your name: ')
print( 'Hello ' + name)
