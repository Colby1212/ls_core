# create a function that takes a list of numbers as an argument

# For each number, determine how many numbers in the list are smaller than it

# When counting number,s onlyy count unique values. 

# That is if a number occurs multiple times it should only be counted once

# input --> list of numbers
# output --> a list of numbers that corresponds to how many numbers are smaller than the number in the original list

# Examples and test cases 

# print(smaller_numbers_than_current([8, 1, 2, 2, 3]) == [3, 0, 1, 1, 2])
# print(smaller_numbers_than_current([7, 7, 7, 7]) == [0, 0, 0, 0])
# print(smaller_numbers_than_current([6, 5, 4, 8]) == [2, 1, 0, 3])
# print(smaller_numbers_than_current([1]) == [0])

# my_list = [1, 4, 6, 8, 13, 2, 4, 5, 4]
# result   = [0, 2, 4, 5, 6, 1, 2, 3, 2]
# print(smaller_numbers_than_current(my_list) == result)



# data types

# Integers, collections

# Algorithm

# Iterate over each number in the list
# Compare the current number to each unique number in the list
# count how many numbers are SMALLER than the current number
# repeat for each number in the list


# code:

def smaller_numbers_than_current(lst):
    result = []
    for num in lst:
        count = 0 
        for unique_num in set(lst):
            if unique_num < num:
                count += 1
        result.append(count)
    return result


print(smaller_numbers_than_current([8, 1, 2, 2, 3]) == [3, 0, 1, 1, 2])
print(smaller_numbers_than_current([7, 7, 7, 7]) == [0, 0, 0, 0])
print(smaller_numbers_than_current([6, 5, 4, 8]) == [2, 1, 0, 3])
print(smaller_numbers_than_current([1]) == [0])

my_list = [1, 4, 6, 8, 13, 2, 4, 5, 4]
result   = [0, 2, 4, 5, 6, 1, 2, 3, 2]
print(smaller_numbers_than_current(my_list) == result)
