# a block word is a word that can be spelled using a specific set of character blocks
# write a function that takes a word string as an argument and returns True if the word
# can be spelled with the set of blocks

# Each block can only be used once:

# The blocks are 

# B:O   X:K   D:Q   C:P   N:A
# G:T   R:E   F:S   J:W   H:U
# V:I   L:Y   Z:M

# examples:

# print(is_block_word('BATCH'))      # True
# print(is_block_word('BUTCH'))      # False --> because both U and H are on the same block 
# print(is_block_word('jest'))       # True
# print(is_block_word('floW'))       # True
# print(is_block_word('APPLE'))      # False --> because they are double letter 
# print(is_block_word('apple'))      # False
# print(is_block_word('apPLE'))      # False
# print(is_block_word('Box'))        # Fals


# basically the question is asking us to see if the the word contains both letters from any of the blocks
# also it should be case sensitive
# also double letters should return false


# Data types:
# collections, strings, booleans


# Algorithm
#create a collection that tracks the blocks that have already been used
#create a collection that contains the blocks
# because it is case insensitive, convert the word to uppercase
# iterate through each character in the word
# for each character, iterate through the blocks
# If the character is found in a block add that box to the collection that tracks used blocks
# Continue to the next characters. IF at any point a character is found in a block that has already been used, return False. 
#Return True if we finish going through the word without returning False


def is_block_word(word):
    blocks = [{'B','O'}, {'X','K'}, {'D','Q'}, {'C','P'}, {'N','A'}, 
              {'G','T'}, {'R','E'}, {'F','S'}, {'J','W'}, {'H','U'}, 
              {'V','I'}, {'L','Y'}, {'Z','M'}]
    has_appeared = []
    for char in word.upper():
        for idx in range(len(blocks)):
            if idx in has_appeared and char in blocks[idx]:
                return False
            if char in blocks[idx]:
                has_appeared.append(idx)
                break
    return True


print(is_block_word('BATCH'))      # True
print(is_block_word('BUTCH'))      # False --> because both U and H are on the same block 
print(is_block_word('jest'))       # True
print(is_block_word('floW'))       # True
print(is_block_word('APPLE'))      # False --> because they are double letter 
print(is_block_word('apple'))      # False
print(is_block_word('apPLE'))      # False
print(is_block_word('Box'))        # False