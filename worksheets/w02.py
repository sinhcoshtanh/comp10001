"""
Floating point calculation
Write a single expression to calculate 5.345x10^5 + 2.14 x 10^2, and print the
result as a float.
"""

print(float( (5.345 * 1e5) + (2.14 * 1e2) ))

"""
Type conversion exercise 1
Write a Python program that asks the user for two numbers val1 and val2 using
the input function, and prints their difference as a float.
"""

val1 = float(input("Enter val1: "))
val2 = float(input("Enter val2: "))

# Calculating the difference
dif = float(val1 - val2)

print(dif)

"""
Type conversion exercise 2
Write a Python program that asks the user for one integer volume (a volume in
millilitres), converts it to litres, and prints the result with l as the units
(for "litre").
"""

vol_in_ml = float(input("Enter volume in ml: "))

# Calculating the volume in L
vol_in_l = int(vol_in_ml % 1000)
vol_str = str(vol_in_l) + "l"

print(vol_str)

"""
Happy Birthday Mr Frodo
It's been a long time since Frodo went out on his Big Adventure. He has lost
track of time, and wonders whether it is his birthday yet. Luckily, he remembers
exactly how many days have passed since he was born. To help Mr Frodo, write a
Python program that asks the user for the number of days since they were born,
and returns their age in years, and the number of days until their next 
birthday.
"""

days_lived = float(input("How many days have you lived? "))

# Calculating the number of years
years_lived = float(days_lived // 365)

# Calculating the remaining days out of 365 days
days_until_birthday = 365 - (days_lived % 365)

msg1 = "You are " + str(years_lived) + " years young!"
msg2 = "You have " + str(days_until_birthday) + "days until you next get to boogie down"

"""
Mr Frodo goes to the bank
Mr Frodo received lots of money for his Birthday. Mr Frodo decided to put it in
the bank. Mr Frodo is clever. He knows that his interest will compound monthly
at a rate of 4.5% p.a. Write a program that asks Mr Frodo how much he is
investing, and for how long (in days), and prints the amount of money he will 
have after this amount of time. You should assume non-empty, integer inputs for
both answers, and assume there are exactly 31 days in every month according to
this bank.
"""

rate = 0.045

amount = input("How much money would you like to invest, Mr Frodo? ")
time = input("How many days would you like to invest this for? ")

# Calculating the final amount by using the provided formula
final_amount = str(amount * (1+rate/12)**(time//31))

print("After that time you will have: $" + final_amount)