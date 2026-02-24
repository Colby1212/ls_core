# create a function that returns the count of distinct case-insensitive alphabetic characters and number digits that occur more than once in the input string 

# You may assume that the input string contains only alphanumeric characters


# Rules
# only alphanumeric characters
# case insensitive
# multiples of characters


# Input --> string
# output--> integer of how many characters appear multiple times


# examples and test cases 


# print(distinct_multiples('xyz') == 0)               # (none)
# print(distinct_multiples('xxyypzzr') == 3)          # x, y, z
# print(distinct_multiples('xXyYpzZr') == 3)          # x, y, z
# print(distinct_multiples('unununium') == 2)         # u, n
# print(distinct_multiples('multiplicity') == 3)      # l, t, i
# print(distinct_multiples('7657') == 1)              # 7
# print(distinct_multiples('3141592653589793') == 4)  # 3, 1, 5, 9
# print(distinct_multiples('2718281828459045') == 5)  # 2, 1, 8, 4, 5


# Data types

# collections, strings, integers


# Algorithm
# create an empty dictionary
# case insensitive --> make the string all lowercase 
# Iterate over each character of the string
# count how many times each character appears
# keep track of each in a dictionary

# Count the amount of characters that appear more than once

# case insensitive --> make the string all lowercase \

# code 


# def distinct_multiples(string):
#     characters = {}
#     string = string.lower()
#     count = 0
#     for char in string:
#         characters[char] = characters.get(char, 0) + 1
#     for character in set(string):
#         if characters[character] > 1:
#             count += 1
#     return count 

# print(distinct_multiples('xyz') == 0)               # (none)
# print(distinct_multiples('xxyypzzr') == 3)          # x, y, z
# print(distinct_multiples('xXyYpzZr') == 3)          # x, y, z
# print(distinct_multiples('unununium') == 2)         # u, n
# print(distinct_multiples('multiplicity') == 3)      # l, t, i
# print(distinct_multiples('7657') == 1)              # 7
# print(distinct_multiples('3141592653589793') == 4)  # 3, 1, 5, 9
# print(distinct_multiples('2718281828459045') == 5)  # 2, 1, 8, 4, 5


def distinct_multiples(string):
    string = string.lower()
    return sum([1 for char in set(string) if string.count(char) > 1])

print(distinct_multiples('xyz') == 0)               # (none)
print(distinct_multiples('xxyypzzr') == 3)          # x, y, z
print(distinct_multiples('xXyYpzZr') == 3)          # x, y, z
print(distinct_multiples('unununium') == 2)         # u, n
print(distinct_multiples('multiplicity') == 3)      # l, t, i
print(distinct_multiples('7657') == 1)              # 7
print(distinct_multiples('3141592653589793') == 4)  # 3, 1, 5, 9
print(distinct_multiples('2718281828459045') == 5)  # 2, 1, 8, 4, 5