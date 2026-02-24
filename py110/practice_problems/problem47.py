# write a function that takes a string argument and returns a new string that contains the words from the argument in reverse order


# Input --> string
# Output --> string

# Rules --> Casing remains the same
# --> Empty strings return an empty string

# examples and test cases 

# Test Cases:
# print(reverse_sentence(''))                       # ''
# print(reverse_sentence('Hello World'))            # 'World Hello'
# print(reverse_sentence('Reverse these words'))    # 'words these Reverse'


# Data types
# Collections, and strings

# algorithm
# create an empty collection 
# add each word in the string to a list in reverse order
# return the list as a string


# Code

def reverse_sentence(string):
    return ' '.join(string.split()[::-1])