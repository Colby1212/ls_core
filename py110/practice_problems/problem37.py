# write a function that takes a string of words separated by spaces, and returns a string in which the first and last letters of every word are swapped.

# You may assume that every word contians at least one letter, the string will always contain at least one word, and each string contains nothing but words an spaces

# input --> String of words
# output --> first and last letter of every word are swapped

# rules --> Every word contains at least one letter? (or two?), String will always be at least one word
# Only words and white spaces


# Examples, and test cases 

# print(swap('Oh what a wonderful day it is') == 'hO thaw a londerfuw yad ti si')
# print(swap('Abcde') == 'ebcdA')
# print(swap('a') == 'a')

# if it is a single letter, the letter remains the same
# Casing is kept. If the first letter is capatalized, a capatalized letter will be at the end of the word

# Data types:
# strings, collections?

# Algorithm
# Iterate over the words of the text
# Each word we swap the first and last letter
# If a word is a single letter, it remains the same 

def swap(text):
    return ' '.join([swap_first_last(word) for word in text.split()])

def swap_first_last(word):
    if len(word) == 1:
        return word
    return word[-1] + word[1:-1] + word[0]


print(swap('Oh what a wonderful day it is') == 'hO thaw a londerfuw yad ti si')
print(swap('Abcde') == 'ebcdA')
print(swap('a') == 'a')