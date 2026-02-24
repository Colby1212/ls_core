# write a function that takes two list arguments, each containing a list of numbers
# and returns a new list containing the product of all combinations of number pairs that can be formed between the two lists

# the return list should be sorted in ascending numerical order


# input --> Two lists
# output --> a sorted list containing the product of all combinations of number pairs that can be formed between the two lists

# rules/assumptions --> the elements in the list will be numbers (integers or floats)

# exmaples:

# list1 = [2, 4]
# list2 = [4, 3, 1, 2]
# print(multiply_all_pairs(list1, list2) == [2, 4, 4, 6, 8, 8, 12, 16])


# repeats are allowed

# we are multiplying --> 2 x 4, 3, 1, and 2, and then we repeat with 4 x 4, 3, 1, 2. there should be 8 items in the list


# data structure --> lists

# algorithm:
# define a function that takes two lists as arguments
# initialize an empty list that will hold the products of each list
# iterate through the first list
#     for each element in the first list, itereate through the second list and multiply the elements together
#     append the product to the empty list
# return a sorted version of teh list from smallest to largest


# Code


def multiply_all_pairs(list1, list2):
    return sorted([num1 * num2 for num1 in list1 for num2 in list2])

list1 = [2, 4]
list2 = [4, 3, 1, 2]
print(multiply_all_pairs(list1, list2) == [2, 4, 4, 6, 8, 8, 12, 16])
