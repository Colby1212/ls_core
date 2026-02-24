# Create a function that takes a list of numbers as an argument
# For each number, determine how many numbers in the list are smaller than it, and place the answer in a list
# when counting numbers, only count unique values. If a number occurs multiple times it should only be counted once

# Inputs --> List of numbers
# Outputs --> List of numbers

# Rules:
# 1. For each number, determine how many in the list are smaller than it
# 2. Each number should only be counted once. (if there are multiple it should only be counted once) 
# 3. return a list that contains how many numbers are smaller than the number. 


# print(smaller_numbers_than_current([8, 1, 2, 2, 3]) == [3, 0, 1, 1, 2])
# print(smaller_numbers_than_current([7, 7, 7, 7]) == [0, 0, 0, 0])
# print(smaller_numbers_than_current([6, 5, 4, 8]) == [2, 1, 0, 3])
# print(smaller_numbers_than_current([1]) == [0])

# my_list = [1, 4, 6, 8, 13, 2, 4, 5, 4]
# result   = [0, 2, 4, 5, 6, 1, 2, 3, 2]
# print(smaller_numbers_than_current(my_list) == result)


# Algorithm
# create a function that takes 1 argument
# iterate over the list and check of unique numbers that are smaller than the number
# add that number to a list
# return the list 


def smaller_numbers_than_current(nums):
    unique_nums = sorted(set(nums))
    return [unique_nums.index(num) for num in nums]


print(smaller_numbers_than_current([8, 1, 2, 2, 3]) == [3, 0, 1, 1, 2])
print(smaller_numbers_than_current([7, 7, 7, 7]) == [0, 0, 0, 0])
print(smaller_numbers_than_current([6, 5, 4, 8]) == [2, 1, 0, 3])
print(smaller_numbers_than_current([1]) == [0])

my_list = [1, 4, 6, 8, 13, 2, 4, 5, 4]
result   = [0, 2, 4, 5, 6, 1, 2, 3, 2]
print(smaller_numbers_than_current(my_list) == result)