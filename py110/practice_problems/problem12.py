# create a function
# it takes a string as an argument
# if the string is a pangram return True
# if it is not return False
# a pangram is a sentence that contains every letter of the alphabet at least once. 
# Case is irrelavent!

# examples

# print(is_pangram('The quick, brown fox jumps over the lazy dog!') == True)
# print(is_pangram('The slow, brown fox jumps over the lazy dog!') == False)
# print(is_pangram("A wizard’s job is to vex chumps quickly in fog.") == True)
# print(is_pangram("A wizard’s task is to vex chumps quickly in fog.") == False)
# print(is_pangram("A wizard’s job is to vex chumps quickly in golf.") == True)

# my_str = 'Sixty zippers were quickly picked from the woven jute bag.'
# print(is_pangram(my_str) == True)

# regardless of case as long as they contain all letters remain True



# data types
# strings, collection

# algorithm
# convert the entire string to lowercase
# use a collection to keep a record of all unique alphabetic characters in the sentence
# go through all unique alphabetic characters in the sentence
# keep track of all the characters seen 
# If there are all 26 letters than it is a pangram, if there isnt than it is not!


# Code
def is_pangram(sentence):
    sentence = set(sentence.lower())
    alphabet_list = (char for char in sentence if char.isalpha())
    return len(alphabet_list) == 26


print(is_pangram('The quick, brown fox jumps over the lazy dog!') == True)
print(is_pangram('The slow, brown fox jumps over the lazy dog!') == False)
print(is_pangram("A wizard’s job is to vex chumps quickly in fog.") == True)
print(is_pangram("A wizard’s task is to vex chumps quickly in fog.") == False)
print(is_pangram("A wizard’s job is to vex chumps quickly in golf.") == True)