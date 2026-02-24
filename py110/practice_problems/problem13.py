# crate a function that takes two strings as arguments
# returns true if some portion of the characters in the first string can be rearranged to match the characters in the second
# Otherwise return False
# Both string arguments only contain lowercase alphabetic characters

# inputs --> Two string arguments
# outputs --> Booleans, True if characters in string 1 can be rearranged to make string 2, False otherwise

# examples:

# print(unscramble('ansucchlohlo', 'launchschool') == True)
# print(unscramble('phyarunstole', 'pythonrules') == True)
# print(unscramble('phyarunstola', 'pythonrules') == False)
# print(unscramble('boldface', 'coal') == True)
# print(unscramble('olc', 'cool') == False)

# Data types
create an empty dictionary for counts in string1
create an empty dictionary for counts in string2
loop thrtough each character of string1 --> Incrtement its count in the dictionary for string 1
loop through each character of string 2 --> Increment its count in the dictionary for string 2
For each character in string2's dictionary --> if string1's count is less than string2's return False
After the loop return True

# Code

def unscramble(string1, string2):
    for char in set(string2):
        if string1.count(char) < string2.count(char):
            return False
    return True
        

print(unscramble('ansucchlohlo', 'launchschool') == True)
print(unscramble('phyarunstole', 'pythonrules') == True)
print(unscramble('phyarunstola', 'pythonrules') == False)
print(unscramble('boldface', 'coal') == True)
print(unscramble('olc', 'cool') == False)