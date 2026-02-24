# create a functioin that returns the count of distinct case insensitive alphabetic/numeric characters
# that occur more than once in the input string
# You may assume that the input string contains only alphanumeric characters

# Input --> string
# Output --> integer of how many characters that appear more than once

# all characters will be alphanumeric
# it will be case INSENSITIVE

# Examples
# print(distinct_multiples('xyz') == 0)               # (none)
# print(distinct_multiples('xxyypzzr') == 3)          # x, y, z
# print(distinct_multiples('xXyYpzZr') == 3)          # x, y, z
# print(distinct_multiples('unununium') == 2)         # u, n
# print(distinct_multiples('multiplicity') == 3)      # l, t, i
# print(distinct_multiples('7657') == 1)              # 7
# print(distinct_multiples('3141592653589793') == 4)  # 3, 1, 5, 9
# print(distinct_multiples('2718281828459045') == 5)  # 2, 1, 8, 4, 5

# Even if the character appears more than twice it is only counted once

# Data structure

# dictionary, string, integer

# Algorithm
# make all characters lowercase because this is case-insensitive
# create a dictionary to track the occurance of each character in the string
# Iterate over the string, increment the counter for each character when it is seen 
# count how many characters appeared more than once
# return the count

# Code

def distinct_multiples(characters):
    characters = characters.lower()
    count = {}
    for char in characters:
        count[char] = count.get(char, 0) + 1
    return len([num for num in count.values() if num > 1])

print(distinct_multiples('xyz') == 0)               # (none)
print(distinct_multiples('xxyypzzr') == 3)          # x, y, z
print(distinct_multiples('xXyYpzZr') == 3)          # x, y, z
print(distinct_multiples('unununium') == 2)         # u, n
print(distinct_multiples('multiplicity') == 3)      # l, t, i
print(distinct_multiples('7657') == 1)              # 7
print(distinct_multiples('3141592653589793') == 4)  # 3, 1, 5, 9
print(distinct_multiples('2718281828459045') == 5)  # 2, 1, 8, 4, 5