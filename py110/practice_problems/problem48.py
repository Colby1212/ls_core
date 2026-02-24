# write a function that takes a string of words as an argument
# The function should revers the letters in every word that has five or more letters, while leacing the others as they are

# input --> string
# output --> string in teh same order but if the words are longer than 5 characters, reverse the letters

# Rules
# Is there puncuation?

# examples and test cases

# Test Cases:
# print(reverse_words('Professional') == "lanoisseforP")
# print(reverse_words('Walk around the block') == "Walk dnuora the kcolb")
# print(reverse_words('Launch School') == "hcnuaL loohcS")

# Data types

# strings, collections, slicing



# algorithm

# iterate over each word in the string
#     -break the string up into individual words

# if the word has atleast 5 characters reverse the letters in the word. (ab = ab , abcde = edcba)

# return the string


# code

def reverse_words(string):
    return ' '.join(word[::-1] if len(word) >= 5 else word for word in string.split())


print(reverse_words('Professional') == "lanoisseforP")
print(reverse_words('Walk around the block') == "Walk dnuora the kcolb")
print(reverse_words('Launch School') == "hcnuaL loohcS")