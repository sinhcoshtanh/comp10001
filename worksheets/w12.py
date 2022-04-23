"""
The function of None return
Write a function mymax() that takes a single argument numlist in the form of
a list of numbers, and returns the highest number in numlist in the case that
it is non-empty, and None otherwise. Note that you may use the built-in
function max() in your code.
"""
def mymax(numlist):

    if not numlist:
        return None

    else:
        return max(numlist)

"""
Multi-returning Functions
Let's write our first function that returns multiple values, using a tuple.

Write a function maxby(intlist) that takes a single argument intlist in the
form of a list of integers, and returns a 2-tuple (maxnum, bymargin), where
maxnum is the maximum integer in the list and bymargin is the difference
between maxnum and the next-highest value.

In the case of a tie for the maximum value, the difference over the next
highest value should be 0. In the case that intlist is an empty list, both
values should be set to None; in the case of a singleton list, bymargin
should be set to None.
"""
def maxby(intlist):
    
    # If the list is empty
    if not intlist:
        return (None, None)
    
    else:
        # If intlist is a singleton list
        if len(intlist) == 1:
            return (intlist[0], None)
    
        # If intlist has more than one entry
        else:
            (bymargin, maxnum) = intlist.sorted()[-2:]
            return (maxnum, maxnum - bymargin)

"""
Timely return
Rewrite the provided code for the function issorted(numlist) that takes a
single argument numlist in the form of a list of numbers, and returns True
if numlist is in increasing sort-order (noting that ties between adjacent
elements are allowed), and False otherwise.

In rewriting the code, you should introduce (at least) one more return
statement, which aborts the function prematurely when a local violation of
the sort-order requirement is detected (expect to fail the first hidden test
if you don't!).

Provided code:

def issorted(numlist):
    sortbool = True
    for i in range(1, len(numlist)):
        if numlist[i] < numlist[i - 1]:
            sortbool = False
    return sortbool
"""

def issorted(numlist):

    for i in range(1, len(numlist)):

        if numlist[i] < numlist[i - 1]:
            return False

    return True

"""
Base-n Number Validation
In a base n number system, all numbers are written using only the digits
{0,1,...,n-1}. For example, in the decimal (= base 10) number system that
you are used to using, all numbers are written using the digits 0,1,..,9,
whereas in the binary (= base 2) number system that your computer uses, all
numbers are written using the digits 0 and 1 only.

Write a function basenum(num, base) that takes as arguments num (a
non-negative integer) and base (a non-negative integer not greater than 10),
and returns True if all digits of num are strictly less than base and False
otherwise (using lazy evaluation). Once again, expect to be tripped up by the
first hidden test if you do not use lazy evaluation.
"""

def basenum(num, base):

    for integer in str(num):
        if int(integer) >= base:
            return False
        
        else:
            return True

"""
Top-5 Words with lambda
Armed with our new knowledge about lambda and sorted()'s key function, let's
return to a previous problem, which should be considerably easier to solve
now.

Write a function top5_words(text) that takes a single argument text (a
non-empty string), tokenises text into words based on whitespace (without
any stripping of punctuation or case normalisation), and returns the top-5
words as a list of strings, in descending order of frequency. If there is a
tie in frequency at any point, the words with the same frequency should be
sub-sorted alphabetically. If there are less than five distinct words in text,
the function should return the words in descending order of frequency (with
the same tie-breaking mechanism).
"""

def top5_words(text):

    tally = {}

    for word in text.split(' '):
        if word not in tally:
            tally[word] = 0
        tally[word] += 1
    
    ranking = sorted(tally, key=lambda x: (-tally[x], x))

    return ranking[:5]
