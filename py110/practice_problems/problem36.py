# write a function that takes a string as an argument
# returns the longest sentence in the text
# as well as its word count
# sentences may end with a ".", '?', or '!'
# Any sequence of characters that are not spaces or sentence-ending characters should be treated as a word. 

# input --> Text of Strings
# output --> '''
#             the longest sentence is: (longest text)
#             It has (word_count) words'
# '''

# Rules:
# words are anything that arent white spaces or sentence ending characters
# Sentence ending characters are . ! ?
# Does the text always end with a sentence ending character?

# return The longest sentence is:
# It has (word_count) words

# Examples

# # Test case 1
# text1 = (
#     "Four score and seven years ago our fathers brought forth on this "
#     "continent a new nation, conceived in liberty, and dedicated to the "
#     "proposition that all men are created equal. Now we are engaged in a "
#     "great civil war, testing whether that nation, or any nation so "
#     "conceived and so dedicated, can long endure. We are met on a great "
#     "battle-field of that war. We have come to dedicate a portion of "
#     "that field, as a final resting place for those who here gave their "
#     "lives that that nation might live. It is altogether fitting and "
#     "proper that we should do this."
# )


# longest_sentence(text1)
# # Expected output:
# # The longest sentence is:
# # "Now we are engaged in a great civil war, testing whether that nation, or any nation so conceived and so dedicated, can long endure."
# # It has 30 words.


# # Test case 2
# text2 = "To be, or not to be, that is the question."
# longest_sentence(text2)
# # Expected output:
# # The longest sentence is:
# # "To be, or not to be, that is the question."
# # It has 10 words.


# # Test case 3
# text3 = "Where do you think you are?"
# longest_sentence(text3)
# # Expected output:
# # The longest sentence is:
# # "Where do you think you are?"
# # It has 6 words.


# Data types
# strings, collections, Integers

# Algorithm

# Break the text up into the individual words
# Iterate through the words
# IF there is a word with a sentence ending character stop there.
# Add the words up until that point to a collection
# Start from the next word and repeat
# find the largest collection of words
# count the words in the collection
# join the words back into a sentence
# return The longest sentence is: followed by the joined sentence and it has (count of words) words. 


# code:

def longest_sentence(text):
    sentence_enders = '!.?'
    word_list = text.split()
    punctuation_idx = [idx +1 for idx in range(len(word_list)) if word_list[idx][-1] in sentence_enders]
    punctuation_idx.insert(0, 0)
    longest_sentence = max([[word for word in word_list[punctuation_idx[idx]: punctuation_idx[idx +1]]] for idx in range(len(punctuation_idx) -1)], key = len)
    length = len(longest_sentence)
    longest_sentence = ' '.join(longest_sentence)
    return f'''
The longest sentence is: 
{longest_sentence}

It has {length} words.
'''

text1 = (
    "Four score and seven years ago our fathers brought forth on this "
    "continent a new nation, conceived in liberty, and dedicated to the "
    "proposition that all men are created equal. Now we are engaged in a "
    "great civil war, testing whether that nation, or any nation so "
    "conceived and so dedicated, can long endure. We are met on a great "
    "battle-field of that war. We have come to dedicate a portion of "
    "that field, as a final resting place for those who here gave their "
    "lives that that nation might live. It is altogether fitting and "
    "proper that we should do this."
)


print(longest_sentence(text1))
# Expected output:
# The longest sentence is:
# "Now we are engaged in a great civil war, testing whether that nation, or any nation so conceived and so dedicated, can long endure."
# It has 30 words.