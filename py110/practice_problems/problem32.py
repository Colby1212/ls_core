# write a function that takes a wrod and list of possible anagrams
# and returns a list of the anagrams

# what are anagrams?
# a word that contains the exact same characters as another (order is not important)

# input 
# word, and a list of strings

# output -->  a list of anagrams

# examples 

# Test Cases:
# print(anagrams('listen', ['enlists', 'google', 'inlets', 'banana']) == ['inlets'])
# print(anagrams('debit card', ['bad credit', 'money', 'documentary']) == ['bad credit'])


# This means that ALL characters are important including white spaces


# data types
# Lists, strings, collections

# algorithm
# 0. Create an empty list to store anagrams
# 1.Iterate over the word and count the instances of each characters
# 2. Store the count
# 3. Iterate over the list and do the same thing, iterate over the word and count each instance of each character
# 4. If the count is exactly the same as the original word, add it to the new list
# 5. return the new list

# Code

def character_count(string):
    characters = {}
    for char in string:
        characters[char] = characters.get(char, 0) + 1
    return characters

def anagrams(string, lst):
    return [anagram for anagram in lst if character_count(anagram) == character_count(string)]

print(anagrams('listen', ['enlists', 'google', 'inlets', 'banana']) == ['inlets'])
print(anagrams('debit card', ['bad credit', 'money', 'documentary']) == ['bad credit'])