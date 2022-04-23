"""
String Indexing
Write a small program that asks the user to enter some text and then 
prints the third character and the third last character of the text they
entered.
"""

text = input("Enter some text: ")

print(text[2])

print(text[-3])

"""
String Slicing and Dicing
For this problem you must write a program that can extract the cost of,
for example, one chocolate bar when given a sentence like How much did 25
chocolate bars cost? $63.75! Your program must first read a sentence from
input. It should then use slicing to get the number of items and the total
cost, and convert those values from strings into numbers. Finally, your
program must calculate and print the cost of a single item.
For this problem, you may assume that the number of items is always 2
digits (that is, it is between 10 and 99 ) and occurs after the phrase
'How much did '. You may also assume that the total cost is always between
10 and 99 dollars with cents (in the form of two digits), and appears at
the end of a sentence (followed with an exclamation mark).
"""

question = input("Question: ")

# Find the number of the items and total cost
num = float(question[13:15])
cost = float(question[-6:-1])

# Converting the cost into cents
cost_in_cents = int(cost * 100)

# Calculating the cost from the cents to the dollars
cost_each_in_cents = float(cost_in_cents // number)

final_dollar = float(cost_each_in_cents // 100)
final_cent = (cost_each_in_cents % 100) / 100

final_cost = '{:.2f}'.format(final_dollar + final_cent)

print(f'${final_cost}')

"""
Your Name, Backwards
Have you ever wondered what your name is written backwards? Write a
program that asks the user for their name and returns it written
backwards. Compare with your classmates and see who would like to be
called by their name written backwards. Apparently, there's a reason we
write our names forwards!
"""

name = input("What is your name? ")

# Reverse the name
reverse = str(name[::-1])

print("Well hello there, " + reverse)

"""
A and an
In English, the indefinite article has two forms: a (used when the first
sound of the following word is a consonant) and an (used, roughly speaking,
when the first sound of the following word is a vowel). As an
oversimplification of how to make this distinction, let's assume that an
should be used when the first letter of the word it precedes is one of a,
e, i, o and u, and a should be used otherwise.
Write a program that asks the user to enter a phrase, and prints out
that phrase preceded by an (with a space) if the phrase starts with a
vowel, and a (with a space) for all other inputs (including the empty
string).
"""

vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

phrase = str(input("Enter a phrase: "))

# https://stackoverflow.com/questions/21617586/reverse-string-string-1-works-but-string0-1-and-others-dont
if phrase[0::-1] in vowel:
    print("an " + phrase)

else:
    print("a " + phrase)

"""
The Culprit
 
James Bond has captured 7 of his arch nemeses. He knows that one of them
is the culprit behind the most dastardly plan in the universe, but is not
sure which one. However, he has a trick up his sleeve. He knows that
Hugo (one of the 7) is not very clever and also that Hugo knows who did it.
So he will present Hugo with a list of names with some confusing
information next to them, and then quickly ask him who did it. Hugo is
smart enough not to say exactly who did it, but he will instead always
say the name of the preceding person in the list, which will be numbered
from 1 to 7 (with a response of 1 indicating that it is person 2, and 7
indicating that the culprit is person 1).
Write a program that asks Hugo to give the number of the culprit, and
returns the name of the person who did it along with the data associated
with that individual (i.e. everything that comes after the name in the
tuple). The list of possible culprits should be stored as a list of tuples,
as below, where each tuple contains a name (a string) and a variable number
of data points associated with that individual (each of which is a string).
Assume the input is a positive integer. The data associated with the
individual must be returned in the form of a tuple (possibly empty).
"""