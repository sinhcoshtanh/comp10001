"""
Canner can
Time to write our first basic function.
Write a function canner_can that takes a single argument item in the form
of a string, and returns the string 'Can you can a [STRING] as a canner
can can a can?', where '[STRING]' takes the value of item.
"""

def canner_can(item):
    return "Can you can a " + item + " as a canner can can a can?'"

"""
Canncer can v2
Having got the basics down pat, let's beef things up a bit more,
building on our first function. You might have noticed in our first
example that we produced strings such as "a apricot" rather than "an
apricot". Let's fix this, based on the simple definition that the
indefinite article should be an if it precedes a vowel, and a for all
other inputs (remember the empty string input!).
Write a function canner_can2 that takes a single argument item in the
form of a string, and returns the string "Can you can an [STRING] as a
canner can can a can?" (where [STRING] takes the value of item) if item
starts with a vowel, and "Can you can a [STRING] as a canner can can a
can?" otherwise. Note that the set of vowels in English is a, e, i, o and
u, and that your function should be able to deal with both upper and
lower-case letters.
"""

vowel = ["A","a","E","e","I","i","O","o"]
word = ""

def canner_can2(item):

    # Use "an" if the word begins with a vowel, add it to the non-empty 
    # string
    if item[0] in vowel:
        word = "an " + item
    
    # Else, use "a", add it to the non-empty string
    else:
        word = "a " + item
    
    return "Can you can " + item + " as a canner can can a can?'"

"""
Goldilocks List
Write a function between_len that takes three arguments:
1. a list words:
2. an integer minlenn: and
3. an integer maxlen
The function should return True if the length of words (as in, the length
of the list, not the words in the list) is at least minlen and no more
than maxlen, and False otherwise.
"""

def between_len(words, minlen, maxlen):

    # Returns whether the length of the list is within the requirements
    return minlen <= len(words) <= maxlen

"""
Word Counter
Explore the methods for strings in the terminal using dir("hello world").
With these in mind, write a function word_count(input_str) that takes a
string as input and returns the number of words in the string.
"""

def word_count(input_str):

    # We split the input and return the length of the input
    return len(input_str.split)