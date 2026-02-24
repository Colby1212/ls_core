# create a function that takes a non-empty string as an argument
# The string consists entirely of lowercase alphabetec characters
# return the length of the longest vowel substring
#  input --> string
#  output --> longest vowel substring

#  rules --> vowels aeiou


#  Examples and test cases

# print(longest_vowel_substring('cwm') == 0)
# print(longest_vowel_substring('many') == 1)
# print(longest_vowel_substring('launchschoolstudents') == 2)
# print(longest_vowel_substring('eau') == 3)
# print(longest_vowel_substring('beauteous') == 3)
# print(longest_vowel_substring('sequoia') == 4)
# print(longest_vowel_substring('miaoued') == 5)

# data types
# collections, strings, integers

# Algorithm
# Iterate over the string, if it is a vowel start the count
# move onto the next character if it is a vowel increment the count
# if it isnt set the count to 0
# return the longest count

# Code

def longest_vowel_substring(string):
    vowels = 'aeiou'
    longest_count = 0
    current_count = 0
    for char in string:
        if char in vowels:
            current_count += 1
        longest_count = max(longest_count, current_count)
        if char not in vowels:
            current_count = 0
    print(longest_count)
    return longest_count 

print(longest_vowel_substring('cwm') == 0)
print(longest_vowel_substring('many') == 1)
print(longest_vowel_substring('launchschoolstudents') == 2)
print(longest_vowel_substring('eau') == 3)
print(longest_vowel_substring('beauteous') == 3)
print(longest_vowel_substring('sequoia') == 4)
print(longest_vowel_substring('miaoued') == 5)