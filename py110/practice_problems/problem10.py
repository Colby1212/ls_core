# create a function that takes a string of digits as an argument and returns the number of even numbered strings that can be formed
# input --> string of numbers
# output --> number of even numbered substrings (strings that end in 0, 2, 4, 6, 8)

# rules:
# if a substring occurs more than once, you should ocunt each as a separate substring

# examples 

# print(even_substrings('1432') == 6)
# print(even_substrings('3145926') == 16)
# print(even_substrings('2718281') == 16)
# print(even_substrings('13579') == 0)
# print(even_substrings('143232') == 12)



# data types
# strings, slicing, integers


# algorithm

# create a collection that includes 0,2 , 4, 6, 8
# create a variable that keeps track of the number of even substrings we can make
# check each number in the string, if the number is an even number, we count how many characters are in the string up to that point
# that determines how many substrings can be made with that even number
# we increment the counter by that amount until we go through all the numbers
# return the counter we created


# Code
def even_substrings(nums):
    evens = '02468'
    evens_counter = 0 
    for idx in range(len(nums)):
        if nums[idx] in evens:
            evens_counter += idx +1 
    return evens_counter

print(even_substrings('1432') == 6)
print(even_substrings('3145926') == 16)
print(even_substrings('2718281') == 16)
print(even_substrings('13579') == 0)
print(even_substrings('143232') == 12)