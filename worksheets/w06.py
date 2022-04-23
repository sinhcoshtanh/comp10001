"""
Dodgy Brother's Dozen
It is a common practice in retail to offer discounts on the unit price
for bulk purchases, and an expectation that when the prices for a given
item are advertised on a per-item and bulk manner, the bulk price will be
cheaper. Unscrupulous operators such as the Dodgy Brothers can sometimes
abuse this expectation, in marking up the bulk price for the unwary.
Write a function dodgy_markup(price) which takes a single (non-negative)
float argument price, and uses a single f-string to return a string of the
following form, where the unit-price is set to price, and the per-dozen
price is set to price multiplied by 12, with a 10% markup. Note that all
prices must be presented in dollars and cents (i.e. to exactly two-decimal
places). 
"""

def dodgy_markup(price):

    # Calculate the price of the dozen with markup
    mk_up = (int(price) * 12) * 1.1

    return f"${price}, or a crazy, crazy ${mk_up} per dozen!"

"""
Dodgy Brothers Price List
The Dodgy Brothers sell a remarkable array of objects, all of dubious
nature, and all at outlandish prices. To help them stay on top of their
inventory, write a function dodgy_inventorise(item) which takes a single
tuple argument item (containing an item volume, description and price,
respectively), and uses an f-string to present the item as a fixed-width
column, where the item volume is up to 6 characters and left-justified,
name is up to 20 characters (with any additional characters ignored) and
right-justified, and the price is up to 10 characters (in dollars and cents)
and right-justified. You can assume that all prices are under $10,000,000,
and all volumes are integers, under 100000. 
"""

def dodgy_inventorise(item):

    # Reminder space.lengthtype
    return f"{item[0]:<6d}{item[1]:>20.20s}{item[2]:>10.2f}"