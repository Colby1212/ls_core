# The fibonacci series is a sequence of numbers in which each number is the sum of the two preceding ones

# write a function that calculates the index of the first fibonacci number that has the number of digits specified by the argument

# input --> a number
# output --> a number that represents the index at which the length of the number in the fibonacci sequence matches the input

# rules --> The fibonacci series starts with 0 and 1

# Test cases and examples 



# Test Cases:
# print(find_fibonacci_index_by_length(2) == 7)
# print(find_fibonacci_index_by_length(3) == 12)
# print(find_fibonacci_index_by_length(10) == 45)
# print(find_fibonacci_index_by_length(16) == 74)
# print(find_fibonacci_index_by_length(100) == 476)
# print(find_fibonacci_index_by_length(1000) == 4782)
# print(find_fibonacci_index_by_length(10000) == 47847)
# 0, 1, 1, 2, 3, 5, 8, 13

# indexes start at 0

# Data types:
# collections, Integers

# algorithm
# Create a list that contains the starting two numbers of the fibonacci sequence (0,1)
# if the length of the last number is not equal to the input, find the next number
# repeat until it is
# return the index of the last number
# Code:


def find_fibonacci_index_by_length(num):
    fibonacci = [0, 1]
    while num != len(str(fibonacci[-1])):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return len(fibonacci) - 1


print(find_fibonacci_index_by_length(2) == 7)
print(find_fibonacci_index_by_length(3) == 12)
print(find_fibonacci_index_by_length(10) == 45)
print(find_fibonacci_index_by_length(16) == 74)
print(find_fibonacci_index_by_length(100) == 476)
print(find_fibonacci_index_by_length(1000) == 4782)
print(find_fibonacci_index_by_length(10000) == 47847)