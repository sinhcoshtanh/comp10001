#-------------------------------------------------------------------------------
"""
while Loop
Write a program that takes values num and N as input and prints the first N
lines of an exponential table for num starting from 1, where both N and num
are strictly positive integers. 
"""

from typing import Counter


num = input("Enter the number for 'num': ")
N = input("Enter the number for 'N': ")

# Determine whether the inputs are digits
if num.isdigit() and N.isdigit():

    # Test for '0' inputs
    if num > 0 and N > 0:

        # Convert 'num' and 'N' into integers
        num = int(num)
        N = int(N)

        # While loop to to print the exponential table
        count = 1
        while count <= N:
            print(f'{count} ** {num} = {count**num}')
            count += 1

else:
    print("Invalid input")

"""
Word formation problem
In this problem you will write a program that prints a list of words that
share the same suffix. First, your program must ask the user to enter all
of the words separated by a space. Then your program must ask for the
common suffix shared by every word. Form words by taking each word and
adding the second string to it.

For example, if the initial words are bake cake lake make rake take wake
and the suffix is s, then the first word will be bakes (bake + s),
followed by cakes, lakes, makes, rakes, takes, and wakes.

Your program should generate all the words and print them one line at a
time. Use the .split() method to turn the string of words into a list and\
then use a for loop to access each word. 
"""

words = input("Enter the list of words: ")
suffix = input("Enter the common suffix: ")
lst_prefix = words.split()

for word in lst_prefix:
    print(f"{word}s")

"""
Gamertag Problem
A gamer's tag is a distinct username you use to identify yourself in an
online gaming community. With the size of such communities growing, it is
highly likely that a simple tag such as your name might already be taken.
You could still choose to use your name as the tag albeit with slight
modifications like inserting a hyphen (-) after each letter. For example,
if your name is Sandy, the gamer's tag would be S-a-n-d-y-.
"""

def make_gamertag(name):

gamertag = ''
    
for letter in name:
    gamertag = letter + '-'
    
return gamertag

"""
For a While...
 
Let's put this into action, in rewriting a while loop to a for loop, in
the context of the provided function allnum(strlist), which takes a list
of strings strlist, and returns the list of strings which are made up
exclusively of digits (in the same order the strings occurred in the
original).

Note that the rewritten function should behave identically to the original,
and the only changes you should make are to the while loop and associated
variables, to rewrite it as a for loop. Note also that in the rewritten
version of the code, you should iterate over the elements of strlist
directly, without indexing. Submissions which don't conform with both of
these will be rejected, so be sure to follow the requirements of the
problem carefully!
"""

def allnum(strlist):
    
    # Empty list to append to make the final list
    final_list = []

    # Iterate over the values within 'strlist'
    for value in strlist:

        # Check whether 'value' is a digit
        if value.isdigit():
            final_list.append(value)
        
    return final_list

"""
While a For...

OK, time now to rewrite a for loop as a while loop.

Mr Frodo is having second thoughts about the trip to Mordor. Being both a
superstitious little chap and a Dungeons and Dragons fan, he carries a
20-sided die wherever he goes. He decides that he will roll the die a
fixed number of times, and if his favourite number comes up, he will go
to Mordor, and if not, he will return to the Shire. We will simulate the
20-sided die through the use of the randint function from the random
library (a topic that we will cover properly in Worksheet 13; for now,
just accept that from random import randint gives you access to the
function, which returns a random integer between the values of the first
and second arguments, inclusive).

Given the provided function luck_tester(lucky_number, max_rolls, die_size),
which takes as arguments: (1) a lucky number lucky_number (3 in Mr Frodo's
case: the number of trolls his uncle encountered in the Trollshaws); (2)
the maximum number of die rolls max_rolls; and (3) the die size die_size
(in terms of the number of sides the die has; 20 in Mr Frodo's case); all
can be assumed to be integers. The function should return a string, of
value depending on whether the lucky number comes up in the provided
number of rolls of the die or not; the precise strings are provided in the
original code.

Note that rewritten function should behave identically to the original,
and the only changes you should make are to the for loop and associated
variables, to rewrite it as a while loop. Submissions which don't do this
will be rejected, so be sure to follow the requirements of the problem
carefully!
"""

def luck_tester(lucky_number, max_rolls, die_size):
    from random import randint

    count = 0
    while count < max_rolls:
        if randint(1, die_size) == lucky_number:
            return 'Off to Mordor!'
        count += 1

    return 'Back to the shire!'

"""
Left Alligned Triangle
Write a program that uses iteration to print a left-aligned right-angled
isosceles triangle with a height specified by the user's keyboard input
(a non-negative integer). 
"""

height = int(input("Enter height: "))

count = 1

while count < height:
    print('*' * count)
    count += 1

"""
Diamond
Write a program to print a diamond made up of left- and right-aligned
right-angled isosceles triangles, all of positive integer height specified
by the user's keyboard input (a positive integer).
"""

height = int(input("Enter triangle height: "))

count = height

while height > 1:
    print('*' * count)
    count -= 1

while count <= height:
    print('*' * count)
    count += 1

"""
Credit Card Validation
Assume that the Internet connection at your retail store is temporarily
down and you need to quickly validate a customer's credit card number
before sending it off for debit authorization. For our purposes, a credit
card number is valid if it has 16 digits and the sum of all digits is a
multiple of 10, and invalid otherwise. Write a function 
validate_card(cardnum) which takes a string of digits cardnum as input
(e.g. '1111111111120133') and returns True if cardnum is a valid credit
card number, and False otherwise.
"""

def validate_card(cardnum):
        
    total = 0
    for number in cardnum:
        total += int(number)

    if len(cardnum) == 16 and total % 10 != 0:
        return True

    else:
        return False