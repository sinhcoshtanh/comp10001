#------------------------------------------------------------------------------
"""
Capital City Testing
Write a function is_capital(state, city) that returns True if the named city 
is the capital of the named state, and False otherwise. Every city and state
in the following table should be recognised.

|=====================|=====================|
|       State         |    Capital city     |
|=====================|=====================|
| New South Wales     | Sydney              |
|---------------------|---------------------|
| Queensland          | Brisbane            |
|---------------------|---------------------|
| South Australia     | Adelaide            |
|---------------------|---------------------|
| Tasmania            | Hobart              |
|---------------------|---------------------|
| Victoria            | Melbourne           |
|---------------------|---------------------|
| Western Australia   | Perth               |
|---------------------|---------------------|
"""

# Dictionary of capitals to later be referenced back to
capitals = {
    'Victoria': 'Melbourne',
    'New South Wales': 'Sydney',
    'Queensland': 'Brisbane',
    'Tasmania': 'Hobart',
    'South Australia': 'Adelaide',
    'Western Australia': 'Perth'
    }

def is_capital(state, city):

    # Checks whether the state is valid in the dictionary
    if state in capitals:

        # Checks whether the associated capital city matches 'city'
        if capitals[state] == city:
            return True
        
        else:
            return False
    
    else:
        return False

"""
Duplicate Word
Write a function repeat_word_count(text, n) that takes a string text and
a positive integer n, converts text into a list of words based on simple
whitespace separation (with no removal of punctuation or changing of case),
and returns a sorted list of words that occur n or more times in text.
"""

def repeat_word_count(text, n):
    
    # We create a dictionary of each word's frequency
    tally = {}
    for word in text.split():
        if word not in tally:
        
            tally[word] = 1
        
        else:
            tally[word] += 1

    repeat_list = []

    for word in tally:
        if tally[word] >= n:
            repeat_list.append(word)
        
    return(sorted(repeat_list))

"""
Mode List
Write a function mode(numlist) that takes a single argument numlist
(a non-empty list of numbers), and returns the sorted list of numbers
which appear with the highest frequency in numlist (i.e. the mode, except
that we want to be able to deal with the possibility of there being
multiple mode values, and hence use a list ... and sort the mode values
while we are at it ... obviously).
"""

def mode(numlist):

    # A tally dictionary to keep track of each number's frequency
    tally = {}

    for num in numlist:
    
    # Checks whether the num in numlist is already in the tally, if not it
    # will create a new entry for it
        if num in tally:
            tally[num] += 1

        else:
            tally[num] = 1

    # Comparing each entry's frequency within the tally and determining the
    # most frequent word/s
    max_freq = 0
    max_list = []

    for num in tally:

        # If the num in tally is more frequent than the current mode number
        if tally[num] > max_freq:
            max_list = [num]
            max_freq = tally[num]

        # If the num in tally is equally frequent in the current mode number
        elif tally[num] == max_freq:
            max_list.append(num)

    return sorted(max_list)

"""
Top-5 Frequent Words
Write a function top5_words(text) that takes a single argument text (a
non-empty string), tokenises text into words based on whitespace (once
again, without any stripping of punctuation or case normalisation), and
returns the top-5 words as a list of strings, in descending order of
frequency. If there is a tie in frequency at any point, the words with
the same frequency should be sub-sorted alphabetically (e.g. if 'turtle'
and 'grok' both occur 5 times, 'grok' should come first). If there are
less than five distinct words in text, the function should return all
words in descending order of frequency (with the same tie-breaking
mechanism).
"""

def top5_words(text):

    # Create a dictionary of a tally of each word's frequency
    tally = {}
    for word in text.split():
        if word not in tally:
            tally[word] = 0
        tally[word] += 1

    # As it is not possible to sort a dictionary we must create a tuple (so
    # we don't risk mutating the object)
    word_list = []
    for (word, freq) in tally.items():
        word_list.append( (-freq, word) ) # sorted() depends on first value
    
    most_5 = []
    for neg_freq, word in sorted(word_list)[:5]:
        most_5.append(word)

    return most_5

"""
Mutual Friends
Write a function mutual_friends(list1, list2) that takes two lists of
friends (with the guarantee of there being no repeat names in either list),
and returns the number of friends in common based on sets.
"""

def mutual_friends(list1, list2):

    # It is important to note that '&' returns the 'middle' or what it shared
    # while 'and' is logical and tests if both are True

    return len(set(list1) & set(list2))