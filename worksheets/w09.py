"""
Cycling Lists
Write a function cycle(input_list) that performs an "in-place" cycling of
the elements of a list, moving each element one position earlier in the
list. Here "in place" means the operation should be performed by mutating
the original list, and your function should not return anything. Note that
you may assume that input_list is non-empty (i.e. contains at least one
element).
"""

def cycle(input_list):
    
    first = input_list[0]

    # Move each position 'down' by 1 place
    for place in range(len(input_list) - 1):
        input_list[place] =  input_list[place + 1]

    # As we did not make a new list, rather change the values of positions
    # other than the last we now must change the last position to the first
    # Example:
    # input_list = [a,b,c,d,e]
    # After iteration input_list = [b,c,d,e,e]
    input_list[-1] = first

    return first

"""
ReCycling Lists
Now write a function cycle(input_list) that performs a cycling of the
elements of a list as before, but this time returns the result as a new
object and does not mutate the input argument.
"""
def cycle(input_list):

    new_list = input_list.copy()
    
    first = new_list[0]
    
    # Move each position 'down' by 1 place
    for place in range(len(new_list) - 1):
        new_list[place] = new_list[place + 1]

    # As we did not make a new list, rather change the values of positions
    # other than the last we now must change the last position to the first
    # Example:
    # input_list = [a,b,c,d,e]
    # After iteration input_list = [b,c,d,e,e]
    new_list[-1] = first
    
    return new_list

"""
for Loop with append
Use a for loop with a break statement and the .append() method to write a function
wordlist(text) that takes a single argument text in the form of a string, and returns a list
of all space-separated words in text made up of letters and numbers ("alphanumeric"
characters) only, up until the first word which contains a non-alphanumeric character (and no
words beyond that point).
"""
def wordlist(text):
    
    # Empty list in order to return at the end
    words = []

    # Iterate over the text individually per word
    for word in text.split():

        # Check whether the word in the iteration is an alphanumeric character
        if word.isalum():
            words = words.append(word)
        
        else:
            break

    return words

"""
Sorted Words
Write a function sorted_words(wordlist) that takes a single list-of-words argument wordlist,
and returns a sorted list of the words in wordlist where the letters are alphabetically
sorted. An example of such a word is door, as there is no letter in the word that has a higher
Unicode value than any letter that follows it, whereas cat is not, as c precedes a in the word
(hint: the sorted() function may come in handy in testing whether the letters in a word are
alphabetically sorted or not). 
"""

def sorted_words(wordlist):

    final_list = []

    for word in wordlist:

        # The sorted function will organise the letters in alphabetical order. If the order is
        # equal to the originally spelling of the word it will append to 'final_list'
        if sorted(word) == list(word):
            final_list.append(word)

        return final_list

"""
Preceding Word Length
Your job is to write the function prevword_ave_len(word) which takes a single argument word
(a str) and returns the average length (in characters) of the word that precedes word in the
text each time it appears. That is, for each occurrence of word in the text, you are to
determine the (single) word which precedes it, and calculate the average length of all those
preceding words. If one of the occurrences of word happens to be the first word occurring in
the text, the length of the preceding word for that occurrence should be counted as zero.
In the instance that word doesn't occur in the text, the function should return -1. Note that
we define a "word" to simply be a string that is delimited by "whitespace" (i.e. punctuation
following a word is included as part of the word). Additionally, the casing in the original
text (and in word) should be preserved.
"""

moby = "Call me Ishmael. Some years ago - never mind how long precisely - having little orno money in my purse, and nothing particular to interest me on shore, I thought I would sail about a little and see the watery part of the world. It is a way I have of driving off the spleen and regulating the circulation. Whenever I find myself growing grim about the mouth; whenever it is a damp, drizzly November in my soul; whenever I find myself involuntarily pausing before coffin warehouses, and bringing up the rear of every funeral I meet; and especially whenever my hypos get such an upper hand of me, that it requires a strong moral principle to prevent me from deliberately stepping into the street, and methodically knocking people's hats off - then, I account it high time to get to sea as soon as I can. This is my substitute for pistol and ball. With a philosophical flourish Cato throws himself upon his sword; I quietly take to the ship. There is nothing surprising in this. If they but knew it, almost all men in their degree, some time or other, cherish very nearly the same feelings towards the ocean with me."

def preword_ave_len(word):
    old_word = ''
    total_len = 0
    num_words = 0

    for cur_word in moby.split():
        if cur_word == word:
            total_len += len(old_word)
            num_words += 1
        
        else:
            old_word = cur_word
        
    if num_words != 0:
        return total_len / num_words
    
    else:
        return -1

"""
Find the Middle Word(s)
Your task is to write a function middle_words(word_list) that returns the middle word(s) from
the non-empty list-of-strings word_list. If the length of word_list is an odd number, you
should return a list containing the single middle word; and if the length of word_list is an
even number, you should return a list containing the two middle words, in the same order as
they occurred in the word_list.
"""

def middle_Words(word_list):

    # Calculating the half length and the length of the list
    half_way = int(len(word_list) / 2)
    length = len(word_list)

    # Middle words for even length list
    if length % 2 == 0:
        return word_list[half_way - 1:half_way + 1]
    
    # Middle words for odd length list
    else:
        return word_list[half_way:half_way + 1]

"""
Longest Sentence
Write a function longest_sentence_length(text) that takes a single string argument text and
returns the length of the longest sentence in text, measured in words.
"""

def longest_sentence_length(text):
    
    sentence_list = text.split('.')
    longest_length = 0

    for sentence in sentence_list:
        if len(sentence) > longest_length:
            longest_length = len(sentence)

    return longest_length

"""
Longer, Higher Strings
Write a function long_high_word(wordlist) that takes a non-empty list of words wordlist (each
of which is a string), and returns the word which is longest, and in the instance of multiple
words having that length, is highest among them, based on Unicode sort order.
"""

def long_high_word(wordlist):

    longest_word = wordlist[0]
    longest_length = len(longest_word)

    for word in wordlist[1:]:

        # Tests whether the word's length is larger than the current longest word or the
        # 'largest' of two equally long words
        if len(word) > longest_length or (len(word) == longest_length and word > longest_word)
            longest_word = word
            longest_length = len(word)
        
    return longest_word