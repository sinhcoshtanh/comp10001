"""
Forgetful Karaoke
Write a function approximate_song(filename) that reads the lyrics of the song in the file of
name filename, and returns the most common word in the song. In the event of a tie, your
function should return the word that comes first alphabetically. Assume that words are
whitespace-delimited, and use .split() with no stripping of punctuation or folding of case to
extract the words from the text.

We have provided lyrics for three songs for you to test your function: somebody.txt,
barbrastreisand.txt, and fakesong.txt. Note these are not the only files we will use to test
your code.
"""

from collections import defaultdict

def approximate_song(filename):
    file = open(filename)
    text = file.read()
    file.close()

    text_list = text.split()
    word_freq = defaultdict(int)

    for word in text_list:
        word_freq[word] += 1

    most_freq = sorted(word_freq, key=lambda x: (-word_freq[x], x))

    return most_freq[0]

"""
Concatenate Files
Write a function concatenate_files(filename1, filename2, new_filename)
that concatenates the text from two source files such that the text from
the file named by argument filename2 follows the text from filename1. The
concatenated text should be written to a new file with the name given by
new_filename. Your function must not return anything.
"""

# Create a function that concatenate filename1 and filename 2 together
def concatenation(file_in, file_out):
    
    copy_file = open(file_in)
    file_out.write(copy_file.read())
    copy_file.close

def concatenate_files(filename1, filename2, new_filename):

    # 'w' creates a new file to be written in
    file_out = open(new_filename, 'w')

    # Calls the function 'concatenation' in order to write within the file
    # 'file_out'
    concatenation(filename1, file_out)
    concatenation(filename2, file_out)
    file_out.close()

"""
Sorting CSV Records
Write a function sort_records(csv_filename, new_filename) that sorts the
records of a CSV file and writes the results as a new CSV file. The first
column of the CSV file will be the city name. The rest of the columns will
be months of the year. The first row of the CSV file will take the form of
the column headings, with all columns other than the first being months of
the year.
"""

import csv

def sort_records(csv_filename, new_filename):

    # Opening and reading the CSV file
    opened_file = open(csv_filename)
    data = csv.reader(opened_file)

    # Creating a separate line or the header
    header = next(data)

    # Convert the data into 2D data then sort the data alphabetically
    data_2d = list(data)
    data_2d.sort()

    opened_file.close()

    # Write the extracted data into a new file 'final_file'
    final_file = open(new_filename, 'w')
    writer = csv.writer(final_file)
    writer.writerow(header)
    writer.writerows(data_2d)
    final_file.close()


"""
Hottest Month
Write a function max_city_temp(csv_filename, city) which analyses
temperatures recorded in a CSV file, and returns the maximum temperature
recorded for the named city.

Once again, the first column of the CSV file will be the city name, and the
rest of the columns will be months of the year. The first row of the CSV
file will provide the column headings. 
"""

import csv

def max_city_temp(csv_filename, city):

    # Open the CSV file
    opened_file = open(csv_filename)
    data = csv.reader(opened_file)

    # Ignoring the header as it does not hold any form of data
    next(data)

    max_temp = 0

    for row in data:
        if row[0] == city:
            max_temp == float(row[1])
            for temp in row[2:]:
                if float(temp) > max_temp:
                    max_temp == temp

    opened_file.close()

    return max_temp

"""
Hottest City
Write a function hottest_city(csv_filename) that analyses the temperatures
recorded in a CSV file, and returns a 2-tuple made up of the maximum
temperature in the whole dataset, along with a sorted list of the names of
cities where that temperature was recorded.

The first column of the CSV file will contain the city name. The rest of
the columns will be months of the year. The first row of the CSV files will
provide column headings.
"""

def hottest_city(csv_filename):

    # Open the CSV file
    opened_file = open(csv_filename)
    data = csv.reader(opened_file)

    # Ignoring the header as it does not hold any form of data
    next(data)

    # Blanks in order to return at the end of the function
    max_city = []
    max_temp = 0

    # Iterates over each row
    # Iterates over each row's temperature
    # determines whether the temperature is larger or equal to the current
    # highest temperature
    for row in data:
        current_city = row[0]
        for temp in row[1:]:
            temp_float = float(temp)
            if temp_float > max_temp:
                max_temp = temp_float
                max_city = [current_city]
            
            elif temp_float == max_temp:
                max_city.append(current_city)
    
    return (max_temp, max_city)
