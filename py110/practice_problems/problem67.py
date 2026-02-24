# create a function that takes a lsit of integers as an argument

# the function should determin the minimum integer value that can be appended to teh list so the sum of all the elements equals the next prime number
# what is a prime number?  a number that can only be divided by 1 and itself 

# rules --> the next prime number, if the sum of the list is already a prime we need the next
# there will always be at least 2 integers, all values in the list must be positive. there may be multiple occurances of numbers on a list

# input --> a list of numbers

# output --> the number that needs to be appended to the list to reach the next prime number


# examples and test cases 

# print(nearest_prime_sum([1, 2, 3]) == 1)        # Nearest prime to 6 is 7
# print(nearest_prime_sum([5, 2]) == 4)           # Nearest prime to 7 is 11
# print(nearest_prime_sum([1, 1, 1]) == 2)        # Nearest prime to 3 is 5
# print(nearest_prime_sum([2, 12, 8, 4, 6]) == 5) # Nearest prime to 32 is 37

# # Nearest prime to 163 is 167
# print(nearest_prime_sum([50, 39, 49, 6, 17, 2]) == 4)



# data types

# Integers, square roots, lists


# Algorithm
# find the sum of the list 
# add one to the sum and check if it is a prime number
# repeat until it is a prime number
# subtract the sum of the list to the next prime number
# return the result 

import math

def nearest_prime_sum(numbers):
    sum_numbers = sum(numbers)
    next_number = sum_numbers + 1
    while not is_prime(next_number):
        next_number += 1
    return next_number - sum_numbers


def is_prime(number):
    if number == 1:
        return False
    squared_num = int(math.sqrt(number))
    for num in range(2, squared_num + 1):
        if number % num == 0:
            return False
    return True

print(nearest_prime_sum([1, 2, 3]) == 1)        # Nearest prime to 6 is 7
print(nearest_prime_sum([5, 2]) == 4)           # Nearest prime to 7 is 11
print(nearest_prime_sum([1, 1, 1]) == 2)        # Nearest prime to 3 is 5
print(nearest_prime_sum([2, 12, 8, 4, 6]) == 5) # Nearest prime to 32 is 37