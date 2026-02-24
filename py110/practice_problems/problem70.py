# create a function that takes a list of numbers,all of which are the same except one
# Find and return the number in the list that differs from all the rest 


# input --> list of numbers
# output --> the odd  number in the list 

# examples and test cases 
# print(what_is_different([0, 1, 0]) == 1)
# print(what_is_different([7, 7, 7, 7.7, 7]) == 7.7)
# print(what_is_different([1, 1, 1, 1, 1, 1, 1, 11, 1, 1, 1, 1]) == 11)
# print(what_is_different([3, 4, 4, 4]) == 3)
# print(what_is_different([4, 4, 4, 3]) == 3)

# data types
# list, integers

# Algorithm
# iterate over the unique numbers in the list. 
# return the one that appears only once 

def what_is_different(numbers):
    return min(numbers, key = numbers.count)