# create a function that takes a string argument and returns the character that occurs most often in the string
# If there are multiple characters with the same frequency, return the one that appears first in teh string
# When  counting characters uppercase and lowercase are the same


# Input --> string
# Output --> Character that appears the most often
# Not case sensitive


# Examples and testcases 

# print(most_common_char('Hello World') == 'l')
# print(most_common_char('Mississippi') == 'i')
# print(most_common_char('Happy birthday!') == 'h')
# print(most_common_char('aaaaaAAAA') == 'a')

# my_str = 'Peter Piper picked a peck of pickled peppers.'
# print(most_common_char(my_str) == 'p')

# my_str = 'Peter Piper repicked a peck of repickled peppers. He did!'
# print(most_common_char(my_str) == 'e')


# All characters, numbers, and spaces included


# Data types

# collections, strings


# Algorithm
# because it is not case sensitive, make all the characters in the string lowercase
# create a dictionary to count the amount of times a character shows up in the string
# Iterate over the list and count the amount of times each character appears in teh string
# return the character that has appeared the most 

# code:


def most_common_char(string):
    string = string.lower()
    character_count = {}
    current_most = 0
    most_frequent = None
    for char in string:
        character_count[char] = character_count.get(char, 0) + 1
    for char in string:
        if character_count[char] > current_most:
            most_frequent = char
            current_most = character_count[char]
    return most_frequent 

print(most_common_char('Hello World') == 'l')
print(most_common_char('Mississippi') == 'i')
print(most_common_char('Happy birthday!') == 'h')
print(most_common_char('aaaaaAAAA') == 'a')

my_str = 'Peter Piper picked a peck of pickled peppers.'
print(most_common_char(my_str) == 'p')

my_str = 'Peter Piper repicked a peck of repickled peppers. He did!'
print(most_common_char(my_str) == 'e')
