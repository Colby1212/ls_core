# create a function that takes a string as an argument
# return True if the string is a panagram

# Pangrams ate senetences that contain every letter of the alphabet at least once. 
# case is irrelavent

# Input --> senetence
# output --> True or False depending on if its a Pangrams


# Examples and data types 

# print(is_pangram('The quick, brown fox jumps over the lazy dog!') == True)
# print(is_pangram('The slow, brown fox jumps over the lazy dog!') == False)
# print(is_pangram("A wizard’s job is to vex chumps quickly in fog.") == True)
# print(is_pangram("A wizard’s task is to vex chumps quickly in fog.") == False)
# print(is_pangram("A wizard’s job is to vex chumps quickly in golf.") == True)

# my_str = 'Sixty zippers were quickly picked from the woven jute bag.'
# print(is_pangram(my_str) == True)

# data types 

# Strings, Booleans


# algorithm
# Iterate over each character of the string
# Count how many unique letters appear
# if there are 26 return True
# If there arent, return False


# code



def is_pangram(string):
    return len(set(char for char in set(string.lower()) if char.isalpha())) == 26

print(is_pangram('The quick, brown fox jumps over the lazy dog!') == True)
print(is_pangram('The slow, brown fox jumps over the lazy dog!') == False)
print(is_pangram("A wizard’s job is to vex chumps quickly in fog.") == True)
print(is_pangram("A wizard’s task is to vex chumps quickly in fog.") == False)
print(is_pangram("A wizard’s job is to vex chumps quickly in golf.") == True)

my_str = 'Sixty zippers were quickly picked from the woven jute bag.'
print(is_pangram(my_str) == True)