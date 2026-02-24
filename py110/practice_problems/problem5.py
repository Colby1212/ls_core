# create a function that takes a string argument
# and returns the character that occurs most often in the
# if there are multiple characters with the same greatest frequency, return the one that appears first in the string
# uppercase and lowercase versions are the same

# inputs --> string
# output --> singular character that occured most frequenetly

# test cases:

# print(most_common_char('Hello World') == 'l')
# print(most_common_char('Mississippi') == 'i')
# print(most_common_char('Happy birthday!') == 'h')
# print(most_common_char('aaaaaAAAA') == 'a')

# my_str = 'Peter Piper picked a peck of pickled peppers.'
# print(most_common_char(my_str) == 'p')

# my_str = 'Peter Piper repicked a peck of repickled peppers. He did!'
# print(most_common_char(my_str) == 'e')  

# the returned character is in lowercase. Even though both upper and lower case are the same, we return the lowercase letter

# Data structure
# lists, sets, strings, counts

# algorithm
# 1. Iterate over each character of the string, and count the occurance of each
# 2. Keep track of the one that has appeared the most
# 3. Return the character that has appeared the most. 


# Code:

def most_common_char(string):
    string = string.lower()
    highest_count = 0
    for char in (string):
        if string.count(char) > highest_count:
            highest_count = string.count(char)
            current_char = char
    print(current_char)
    return current_char

print(most_common_char('Hello World') == 'l')
print(most_common_char('Mississippi') == 'i')
print(most_common_char('Happy birthday!') == 'h')
print(most_common_char('aaaaaAAAA') == 'a')