"""
Loose Change
Because we don't use 1 cent coins anymore, when you use cash to buy things
like groceries, the amount is rounded up or down to the nearest 5 cents.
For example if you buy $5.57 worth of carrots, it would get rounded down and
you would pay $5.55 in cash (saving 2 cents!). But $5.58 worth of carrots
would get rounded up and cost $5.60.
Life hack: Always go for the option which is rounded down!
Write a program that takes the cost of an item and tells you whether the cost
stays the same/is rounded down (good, pay in cash), or was rounded up (bad,
you should pay by card).
"""

cost = float(input("How much does it cost? "))

# Calculating the last digit of the remainder
remainder = str(int(cost * 100 ))
x = int(remainder[-1])

if 0 <= x <= 2 or 6 <= x <= 7:
    print("The price didn't change or was rounded down! Pay cash!")
    
else:
    print("The price was rounded up! Pay card.")

"""
Detecting Enemies
Now let's test our skills to help out our friend Jon Snow from Game of Thrones.
He is having a dull moment and wants to use an app to check if people entering
his camp are enemies! Write a simple program that asks the user to enter a
name and determines whether they are enemies or not.
Fortunately for us, Jon Snow has two kinds of enemies: those who can't use
phones, and those who will enter one of 0, 1 or 2, because in their language
name means "dial a number after the prompt" (and they can't count past 
2 ... although, somewhat suspiciously, they do have a zero in their number
system). The enemies who can't use phones obviously won't enter anything,
and should receive the following message: A luddite! GO AWAY AT ONCE!.
The enemies who think that names are single-digit numbers (specifically 0, 1
or 2) should receive: HAHA! You may not pass!!.
Everyone else receives: Welcome to the camp, <name>, if that really is your
name. Where <name> should be replaced by the user's name.
"""

name == str(input("Enter your name, soldier: "))

if name == "0" or "1" or "2":
    print("HAHA! You may not pass!!")

elif name == "":
    print("A luddite! GO AWAY AT ONCE!")

else:
    print("Welcome to the camp, " + name + ", if that really is your name.")

"""
Science Classifier
It's hard to keep up with the pace of progress of science at times, with
new(ish) fields of science with cool-sounding names including proteomics,
quantum biology and computational neurolinguistics. Your job in this exercise
is to write a simple scientific "classifier" which takes the name of a field
of science as input, and prints out a (pithy) comment as follows:
- if it ends with omics, your code should print Life science hippy!
- if it begins with comp or info, your code should print Computing ftw!
- if it ends with y, your code should print Au naturel!
failing all these, your code should print Too new to keep up!
Note that for an input which matches multiple of these conditions, the
first-listed matching condition should apply (and only one message should be
printed out). You may assume that the input will consist entirely of
lower-case characters and spaces
"""

name = str(input("Hit me: "))

if str(name[-5:-1] + name[-1]) == "omics":
    print("Life science hippy!")

elif str(name[0:4]) == "comp" or "info":
    print("Computing ftw!")

elif str(name[-1]):
    print("Au naturel!")

else:
    print("Too new to keep up!")

"""
Season's Greetings
Write a program which asks the user for a month of the year, as a number
between 1 and 12. Your program must then print one of the following messages
depending on the season the specific month falls in:
- It's summer. Have fun in the sun! if the number is 1, 2 or 12.
- It's autumn. Enjoy the beautiful sunsets! if the number is between 3 and 5 
(inclusive).
- It's winter. Go skiing! if the number is between 6 and 8 (inclusive).
- It's spring. Check out the spring racing carnival! if the number is between
9 and 11 (inclusive).
- Your program should print an error message Invalid input. Please enter any
number between 1 and 12. if any other number is encountered.
"""

month = float(input("Enter the month (1-12): "))

if (1 <= month <= 2) or month == 12:
    print("It's summer. Have fun in the sun!")

elif (3 <= month <= 5):
    print("It's autumn. Enjoy the beautiful sunsets!")

elif (6 <= month <= 8):
    print("It's winter. Go skiing!")

elif (9 <= month <= 11):
    print("It's spring. Check out the spring racing carnival!")

else:
    print("Invalid input. Please enter any number between 1 and 12")