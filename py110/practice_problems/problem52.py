# create a function that takes a list of Integers

# The function should return the minimum sum of 5 consecutive numbers in the list
# if the list contains fewer than 5 elements, the funciton should return None


# Input --> a list of numbers
# output --> minimum sum of 5 consecutive numbers
# or None if it is less than 5


# Examples and test cases:

# print(minimum_sum([1, 2, 3, 4]) is None)
# print(minimum_sum([1, 2, 3, 4, 5, -5]) == 9)
# print(minimum_sum([1, 2, 3, 4, 5, 6]) == 15)
# print(minimum_sum([55, 2, 6, 5, 1, 2, 9, 3, 5, 100]) == 16)
# print(minimum_sum([-1, -5, -3, 0, -1, 2, -4]) == -10)


# data types

# lists, integers


# Algorithm

# Iterate over 5 consecutive elements of the list at a time and find the sum
# save the sum onto a variable
# On the next iteration, compare the sum to the current sum 
# if it is smaller than replace the value
# repeat until we reach the 5th last number in the list 
# If the list is shorter than 5 elements, return None


# code

def minimum_sum(numbers):
    if len(numbers) < 5:
        return None

    current_sum = sum(numbers[:5])

    for idx in range(len(numbers) - 4):
        sum_window = sum (numbers[idx: idx +5])
        if sum_window < current_sum:
            current_sum = sum_window

    return current_sum
    

print(minimum_sum([1, 2, 3, 4]) is None)
print(minimum_sum([1, 2, 3, 4, 5, -5]) == 9)
print(minimum_sum([1, 2, 3, 4, 5, 6]) == 15)
print(minimum_sum([55, 2, 6, 5, 1, 2, 9, 3, 5, 100]) == 16)
print(minimum_sum([-1, -5, -3, 0, -1, 2, -4]) == -10)