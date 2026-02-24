# create a function that takes two string as an argument

# Return True if some portion of the characters in the first string can be rearranged to match the characters in the second
# Otherwise return False

# Rules
# You may assume that both string arguments only contian lowercase alphabetic characters
# neither will be empty

# Input --> two Strings
# OUtput --> True or False 

# Examples and test cases 

# print(unscramble('ansucchlohlo', 'launchschool') == True)
# print(unscramble('phyarunstole', 'pythonrules') == True)
# print(unscramble('phyarunstola', 'pythonrules') == False)
# print(unscramble('boldface', 'coal') == True)
# print(unscramble('olc', 'cool') == False)


# data types

# Dictionary, string, boolean, Int 


# Algorithm
# create two dictionaries
#     1. to keep track of the occruance of each character in the first string
#     2. to keep track of the occurance of each character in the second string
# Count the occurance of each character in the first string
# Count the occurance of each character in the second string

# Iterate over the dictionary of the second string, see if the characters in the first string appear atleast as many times as it does in the second string


# if at any point it does not return False
# If they all appear that many times return True

# Code

def unscramble(string1, string2):
    available = {}
    required = {}
    
    for char in string1:
        available[char] = available.get(char, 0) + 1
    
    for char in string2:
        required[char] = required.get(char, 0) + 1

    for char in required:
        if char not in available or available[char] < required[char]:
            return False
    return True


print(unscramble('ansucchlohlo', 'launchschool') == True)
print(unscramble('phyarunstole', 'pythonrules') == True)
print(unscramble('phyarunstola', 'pythonrules') == False)
print(unscramble('boldface', 'coal') == True)
print(unscramble('olc', 'cool') == False)