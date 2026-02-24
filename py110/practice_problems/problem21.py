# wreite a function that takes a string as an argument 
# it returns a new string that contains all the vowels from the original string

# Input --> string
# output --> string

# Test Cases:
# print(select_vowels("launch school") == "auoo")
# print(select_vowels("assessment") == "aee")
# print(select_vowels("RHYTHM") == "")
# print(select_vowels("AEIOU") == "AEIOU")


# Rules --> Case sensitive, the vowels are in order. 
# If there are no vowels, return an empty string


# Data types
# Collection, string

# Algorithm
# create a new string that contains all the vowels (aeiouAEIOU)
# Iterate through the string
# check to see if the character is a vowel
# If it is a vowel add it to a new string
# return the string of vowels

# Code


def select_vowels(string):
    vowels = 'aeiouAEIOU'
    return ''.join(char for char in string if char in vowels)

print(select_vowels("launch school") == "auoo")
print(select_vowels("assessment") == "aee")
print(select_vowels("RHYTHM") == "")
print(select_vowels("AEIOU") == "AEIOU")
