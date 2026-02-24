# write a function that takes as tring and returns a dictionary where the keys are the length of the words
# and the values are the number of words of that length
# Puncuation should be treated as a part of the word


# input --> string
# output --> dictionary
# keys --> length of the word
# values --> number of words of that length 


# rules --> Puncuation should be treated as part of the word

# Examples/test cases 

# print(word_sizes('Four score and seven.') == {4: 1, 5: 1, 3: 1, 6: 1})
# four --> 4 letters
# score --> 5 letters
# and --> 3 letters
# seven. --> 6 letters

# Each of these appear once. 
# The keys are the amount of letters
# the values are how many times they appear

# print(word_sizes('Hey diddle diddle, the cat and the fiddle!') == {3: 5, 6: 1, 7: 2})
# print(word_sizes("What's up doc?") == {6: 1, 2: 1, 4: 1})
# print(word_sizes('') == {})
# Would you like the solutions to any of these questions, or would you like me to explain any of the solutions?
# Did I answer your question?


# algorithm

# Create an empty dictionary
# Iterate over the words of the string
# For each word count how many letters are in it
# Create a key at which the number of letters is the key, and start at a value of 1
# if such key already exists, increase the vlaue by 1



# Code

# def word_sizes(string):
#     word_lengths = {}
#     for word in string.split():
#         word_lengths[len(word)] = word_lengths.get(len(word), 0) + 1
#     return word_lengths

def word_sizes(string):
    lengths = [len(word) for word in string.split()]
    return {n: lengths.count(n) for n in set(lengths)}

print(word_sizes('Hey diddle diddle, the cat and the fiddle!') == {3: 5, 6: 1, 7: 2})
print(word_sizes("What's up doc?") == {6: 1, 2: 1, 4: 1})
print(word_sizes('') == {})
