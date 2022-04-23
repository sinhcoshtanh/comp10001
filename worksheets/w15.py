"""
Disentangling list comprehensions
List comprehensions can be baffling verging on incomprehensible at first
(joke!), so let's get some experience pulling a list comprehension apart
into code that you are more familiar with. Given the following mystery
function, write an equivalent function aha(minval, maxval) with the exact
same functionality but which doesn't make use of list comprehensions.

def mystery(minval, maxval):
    return [i**2 % 10 for i in range(minval, maxval + 1)]
"""
def aha(minval, maxval):
    result = []
    for i in range(minval, maxval + 1):
        result.append(i**2 % 10)

    return result

"""
Hack the System

Write a function hack_it(start, middle, end) which takes three arguments as
input: (1) start, a list of at least two words from which the first part of
the password is formed; (2) middle, a string containing the middle part of
the password; and (3) end, an integer defining the maximum age for the
sysadmin's cat. The function should return a list of all possible password
strings, to use in a brute-force password attack.

Presets:
LIKELY_WORDS = ["Frenchy", "INTENSE", "ComputerScienceFTW", "HelloMrGumby"]
MIDDLE = "Horse20"
CREME_PUFF = 38
"""

from itertools import permutations

def hack_it(start, middle, end):

    # Final passwords list
    passwords = []

    # Handle the permutations of the start list
    for first_part in permutations(start, 2):

        # Adding the numbers from 0 until the current age
        for last_part in range(end + 1):

            # Append the final combination
            # ':02d' makes sure that the first whole numbers are a double digit'
            passwords.append(f"{first_part}{middle}{last_part:02d}")
            
    return passwords
