# create a function that takes a list of integers as an argument
# determine adn return the index N for whcih all numbers with an index less than N sum to the same value as the numbers with an index greater than n
# If there is no index that would make this happen return -1
# If you are given a llsit with multiple answers, return the index with the smallest value

# The sum of the numbers to the left of index 0 is 0
# likewise the sum of of the numbers to the right of the last element is 0


# input --> a list of numbers
# output --> The index at which both the left side and right side are equals
# it is important to note that when looking at an ndex it does not include the number in that index 


# examples and test cases 

# print(equal_sum_index([1, 2, 4, 4, 2, 3, 2]) == 3)
# print(equal_sum_index([7, 99, 51, -48, 0, 4]) == 1)
# print(equal_sum_index([17, 20, 5, -60, 10, 25]) == 0)
# print(equal_sum_index([0, 2, 4, 4, 2, 3, 2]) == -1)

# # The following test case could return 0 or 3. Since we're
# # supposed to return the smallest correct index, the correct
# # return value is 0.
# print(equal_sum_index([0, 20, 10, -60, 5, 25]) == 0)


# data types

# slicing, integers, lists


# Algorithm

# iterate over each index of the list

# if the list on the left is equal to the list on the right in value return the index

# if none of them return the same value than return -1

# code
def equal_sum_index(numbers):
    for idx in range(len(numbers)):
        if sum(numbers[:idx]) == sum(numbers[idx + 1:]):
            return idx

    return -1

print(equal_sum_index([1, 2, 4, 4, 2, 3, 2]) == 3)
print(equal_sum_index([7, 99, 51, -48, 0, 4]) == 1)
print(equal_sum_index([17, 20, 5, -60, 10, 25]) == 0)
print(equal_sum_index([0, 2, 4, 4, 2, 3, 2]) == -1)

# The following test case could return 0 or 3. Since we're
# supposed to return the smallest correct index, the correct
# return value is 0.
print(equal_sum_index([0, 20, 10, -60, 5, 25]) == 0)