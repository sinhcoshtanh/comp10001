"""
Chess Problem v1
Write a function check_move(column, row) which returns a string describing
a chess move to a given row and column on the chess board. Your program
must check if the row and column entered are both valid. The column in a
chess board is a letter ranging from A to H (inclusive, in upper case) and
the row is a number between 1 and 8 (inclusive).
column will be given to your function as a string and row will be given as
an integer.
'A' or 'E' are valid columns but 'a' or 'L' are not (lower case, and out
of range, respectively).
Similarly, 2 and 8 are valid rows but 0 and 9 are not (both are out of
range).
If both coordinates are valid, such as 'E' and 2, your function must
return 'The piece is moved to E2.', otherwise it should return 'The
position is not valid.'.
Note that you can assume that the first argument (the column designator)
is a single-character str, and the second argument (the row designator)
is an int.
"""

def check_move(column, row):

    # Check whether inputs are 1 character and within the size of the chess
    # board
    if len(column) == 1 and 'A' <= column <= 'H' and 1 <= row <= 8:
        return f'The piece is moved to {column}{row}.'
    
    else:
        return "The position is not valid."

"""
Chess Problem v2
Write a new version of your algebraic chess notation validation function
check_move() which also allows lower-case letters for the column designators,
but is otherwise identical to your first version (including outputting the
column designators in upper case, irrespective of the case in the input).
That is, columns such as 'a' or 'f' should now be accepted as well.
Note that you can once again assume that the first argument (the column
designator) is a single-character str, and the second argument (the row
designator) is an int.
"""

def check_move(column, row):

    # Capitalise 'column' to later test whether it is in the range
    up_column = str(column.upper())

    if len(up_column) == 1 and 'A' <= up_column <= 'H' and 1 <= row <= 8:
        return f'The piece is moved to {up_column}{row}.'
    
    else:
        return "The position is not valid."

"""
Chess Problem v3
Let's extend check_move() again, to still allow column designators in 
upper or lower case, but now to provide feedback when there is an error
in the input on whether the error is in the column or row designator:
* If the column value is out of range (regardless of whether the row value
is in or out of range) return 'The column value is not in the range a-h
or A-H!'.
* If the column value is in range but the the row value is out of range,
return 'The row value is not in the range 1 to 8!'.
* If both column and row values are in range, return 'The piece is moved to
<COLUMN><ROW>.' as in the previous problems.
Note that you can still assume that the column designator is a
single-character str, and the row designator is an int.
"""

def check_move(column, row):
    
    # Capitalise 'column' to later test whether it is in the range
    up_column = str(column.upper())

    # Testing whether 'column' is within the range a-h/A-H
    if len(up_column) != 1 or not 'A' <= up_column <= 'H':
        return f'The column value is not in the range a-h or A-H!'
    
    # Testing whether 'row' is within the range 1-8
    elif not 1 <= row <= 8:
        return f'The row value is not in the range 1-8!'
    
    # If the input satisfies the range
    else:
        return f'The piece is moved to {up_column}{row}'

"""
Chess Problem v4
OK, final stop in chess land, extending check_move() again. Previously,
your function took two separate arguments: a column and a row value.
Now you will rewrite the function to accept the board position as a single
str argument. In other words, the input to check_move(position) will now
be a single position string such as 'B5', that encodes both the column and
the row designator.
When both the coordinates in position are valid, for example, 'c4', the
function returns 'The piece is moved to C4.'.
If position has too many or too few characters, return 'The position is not
valid.'
If the column designator is out of range (regardless of whether the row designator is valid or not) return 'The column value is not in the range a-h or A-H!'.
Otherwise, if the row designator is out of range, return 'The row value is not in the range 1 to 8!'.
Note that, irrespective of the casing of the column value, your code should output the value in upper case. Also note that there is no guarantee that the input is made up of exactly two characters.
"""

def check_move(position):

    # Check if the length if valid
    if len(position) != 2:
        return f'The position is not valid.'

    else:
        
        # Extracting the column and row values
        column = str(position[0].upper())
        row = int(position[1])
        
        # Checking whether the column is within the range
        if not 'A' <= column <= 'H':
            return f'The column value is not in the range a-h or A-H!'

        # Checking whether the row is within the range
        if not 1 <= row <= 8:
            return f'The row value is not in the range 1 to 8!'
    
        else:
            return f'The piece is moved to {column}{row}.'

"""
Card Sercurity Code problem
The 3 digit card security code (CSC) on a credit card helps to protect
against credit card fraud. Write a simple function check_csc(code) that
checks if a given code (entered as a string) is valid. For our purposes,
the code is valid if it is exactly three characters long and all three
characters are digits between 0 and 9 (inclusive). If the CSC is valid,
your function must return True. Otherwise it must return False.
"""

def check_csc(code):
    
    if len(code) == 3 and code.isdigit():

        return True
    else:
        return False