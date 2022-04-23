"""
Triangle Leg Lengths
Write a function triangle_legs(hyp, angle) that returns
the lengths of the two sides of a right-angled triangle
that are adjacent to the right angle (i.e. the "legs"),
given the length of the hypotenuse (hyp — a positive
number) and one of the two non-right angles of the
triangle (angle — a positive number in degrees, less
than 90).  The function should return a 2-element tuple
of floats, with the shortest leg first.
"""

from math import sin, cos, radians

def triangle_legs(hyp, angle):
    angle = radians(angle)

    return tuple(sorted([hyp * cos(angle), hyp * sin(angle)]))

"""
Donald Trump's Speech

For this problem you should write two functions. The first
function count_lengths() should take a string text, and
return a default dictionary containing the frequency counts
of each word length. Your function should split text up
into words based on whitespace using the .split() method,
without removing punctuation or changing the case of any of
the "words".

The second function top5_word_lengths() should take a
string text, and return the list of the (up to) five
most-frequent word lengths. It should operate by first
calling count_lengths() over text to generate a dictionary
of word lengths, then sorting the word lengths in terms in
descending order of frequency, and returning the top 5 (or
less in the instance that there aren't 5). In the case of a
tie in frequency, the word lengths should be sub-sorted in
descending order of word length.
"""
from collections import defaultdict

def count_lengths(text):
    
    length_freq = defaultdict(int)
    
    for word in text.split():
        length_freq[len(word)] += 1
    
    return length_freq

def top5_word_lengths(text):

    length_freq = count_lengths(text)

    ranking = sorted(length_freq, key=lambda x: (length_freq[x], x), reverse=True)

    return ranking[:5]

"""
Visualising Factors
Write a program that asks the user for a positive integer limit and prints
a table to visualize all factors of each integer ranging from 1 to limit.
A factor i of a number n is an integer which divides n evenly (i.e.
without remainder). For example, 4 and 5 are factors of 20, but 6 is not.
Each row represents an integer between 1 and 20. The first row represents
the number 1, the second row the number 2, and so forth. For a given
position i (starting from 1) in a row n, '* ' indicates that i is a factor
of n, and '- ' indicates that it is not.
"""

limit = int(input("Maximum number to factorise:"))

for i in range(1, limit + 1):

    line = ''

    for j in range(1, limit + 1):
        
        # If the modudlo division results in a remainder of 0 then the
        # it is a multiple of i
        if i % j == 0:
            line += "* "
        
        else:
            line += "- "
    
    print(line)

"""
Matching Codons
Write a function matching_codons(complements, pool1, pool2) that takes
three arguments: a dictionary complements and two lists pool1 and pool2.
The dictionary contains the base pairs, and the pools each contain a list
of codon sequences. Your task is to find the complementary codon sequence
in pool2 for each codon sequence in pool1, and return all matching pairs.
"""

def matching_codons(complements, pool1, pool2):
    
    list = []

    # For each sequence
    for seq1 in pool1:

        inverse = ''

        # We are producing a tuple much like pool2 in order to examine whether
        # it matches the complement in pool2.
        for letter in seq1:
            inverse += complements[letter]
        
        if inverse in pool2:
            list.append((seq1, inverse))

    return list

"""
Image Grey Value
Write a Python function grey_value(image) which takes an image image (represented as a list of
lists like above) and returns its grey value. The grey value of a black and white picture is
defined as the number of white pixels divided by the total number of pixels in the picture.
Your function should return the grey value as a single floating-point number in the range 0.0
to 1.0.
"""

def grey_value(image):

    pixel_count = 0
    white_count = 0

    for row in image:
        pixel_count += len(row)
        
        for pixel in row:
            white_count += pixel
        
    return white_count / pixel_count
