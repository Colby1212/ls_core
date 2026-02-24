# write a function that takes a strinng argument
# return a list of all substirngs that start from the beginning of the string
# ordered from shortest to longest

# input --> string
# output --> list of substirngs

# rules --> the list should be ordered from shortest to longest
# it should include the full string as the last elemeents
# it starts from the first index and goes to the last

# Examples / test cases 

# Test Cases:
# print(leading_substrings('abc') == ['a', 'ab', 'abc'])
# print(leading_substrings('a') == ['a'])
# print(leading_substrings('xyzzy') == ['x', 'xy', 'xyz', 'xyzz', 'xyzzy'])

# starts at the first index
# then includes the next and so forth 


# Data types 

# strings, substrings, lists 

# Algorithm
# Create an empty list, 
# iterate over each index of the string
# start from idex 0 and go to the last
# keep adding characters of the string to the first to increase the length of the substring
# Each time we add a character we add it to the empty list
# we return the list when we are done iterating over the indexes



# def leading_substrings(string):
#     substrings = []
#     for index in range(len(string)):
#         substrings.append(string[:index +1])
#     return substrings

def leading_substrings(string):
    return [string[:index+1] for index in range(len(string))]


print(leading_substrings('abc') == ['a', 'ab', 'abc'])
print(leading_substrings('a') == ['a'])
print(leading_substrings('xyzzy') == ['x', 'xy', 'xyz', 'xyzz', 'xyzzy'])