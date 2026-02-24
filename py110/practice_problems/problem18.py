# create a function that takes a list of integers as an argument

# Determine and return the index N for which all numbers with an index less than N for which all numbers
# with an index less than N sum to the same value as the numbers with an Index greater than n
# If there is no index that would make this happen, return -1

# IF you are given a list with multiple answers, return the index with the smallest value

# input --> list of numbers
# output --> Index in which the sum of the left and right side are the same

# examples:

# print(equal_sum_index([1, 2, 4, 4, 2, 3, 2]) == 3)
# print(equal_sum_index([7, 99, 51, -48, 0, 4]) == 1)
# print(equal_sum_index([17, 20, 5, -60, 10, 25]) == 0)
# print(equal_sum_index([0, 2, 4, 4, 2, 3, 2]) == -1)

# # The following test case could return 0 or 3. Since we're
# # supposed to return the smallest correct index, the correct
# # return value is 0.
# print(equal_sum_index([0, 20, 10, -60, 5, 25]) == 0)

# neither side includes the indexed number
# if we use the first example index 3 would be 4

# so it would add 1, 2, 4,  or lst[0:3]
# and the other side would be 2, 3, 2 or lst[5:]



# data types
# lists, sum, integers, index


# algorithm
# Iterate over each index in the list
# check if both sides of the number are equivalent to each other. (exclusive of the value at that index)
# when we find an index where that is the case than we return the index
# if we finish going through the list and find no such value, return -1


# Code

def equal_sum_index(numbers):
    for idx in range(len(numbers)):
        if sum(numbers[:idx]) == sum(numbers[idx+1:]):
            return idx
    return -1

print(equal_sum_index([1, 2, 4, 4, 2, 3, 2]) == 3)
print(equal_sum_index([7, 99, 51, -48, 0, 4]) == 1)
print(equal_sum_index([17, 20, 5, -60, 10, 25]) == 0)
print(equal_sum_index([0, 2, 4, 4, 2, 3, 2]) == -1)


def equal_sum_index(numbers):
    total_sum = sum(numbers)
    left_sum = 0

    for idx, num in enumerate(numbers):
        right_sum = total_sum - left_sum - num
        if left_sum == right_sum:
            return idx
        left_sum += num

    return -1