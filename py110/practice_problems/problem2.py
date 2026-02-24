# create a function that takes a list of integers as a argument
# the function should return the minimum sum of 5 consecutvie numbers in the list
# If the list contains less than 5 elements return None

# Input --> list of numbers
# output --> Integer (minimum sum of 5 consecutive numbers)


# The list will always contain only integers
# if there are fewer than 5 numbers return None

# Algorithm
# check for length of list. If less than 5 return None
# Iterate over the list 5 items at a time till the 5th last element
# For each index check the sum
# return the minimum sum

def minimum_sum(nums):
    if len(nums) < 5:
        return None
    return min([sum(nums[idx:idx + 5]) for idx in range(len(nums) -4)])


print(minimum_sum([1, 2, 3, 4]))
print(minimum_sum([1, 2, 3, 4, 5, -5]))
print(minimum_sum([1, 2, 3, 4, 5, 6]))
print(minimum_sum([55, 2, 6, 5, 1, 2, 9, 3, 5, 100]))
print(minimum_sum([-1, -5, -3, 0, -1, 2, -4]))
