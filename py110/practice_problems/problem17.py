# create a function that takes a list of integers
# The function should determine the minimum integer value that can be appended to teh list so the sum of all the elements equals the closest prime number
# that is greater than the sum of the numbers


# The list will always contain 2 integers
# all values in the list must be positive (greater than 0)
# there may be multiple occurances of various numbers(duplicates)

# What is a prime number? --> a number that can only be divided by 1 and itself. 

# Examples:



# # Nearest prime to 163 is 167
# print(nearest_prime_sum([50, 39, 49, 6, 17, 2]) == 4)
# If the number is already a prime number we need to find the NEXT prime number

# Data types
# lists, nums

# Algorithm
# Sum the numbers in the list
# startin from the sum +1 check each consecutive number to see if it is prime
# once a prime number is found, calculate the differenc ebetween the prime and the original
# Return the difference between the next prime and the sum of the total



# Code

import math 

def is_prime(num):
    if num < 2:
        return False
    for factor in range(2, int(math.sqrt(num)) + 1):
        if num % factor == 0:
            return False
    return True


def nearest_prime_sum(numbers):
    next_prime = sum(numbers) + 1
    while not is_prime(next_prime):
            next_prime += 1
    return next_prime - sum(numbers)


print(nearest_prime_sum([1, 2, 3]))        # Nearest prime to 6 is 7
print(nearest_prime_sum([5, 2]))
print(nearest_prime_sum([1, 1, 1]) == 2)        # Nearest prime to 3 is 5
print(nearest_prime_sum([2, 12, 8, 4, 6]) == 5) # Nearest prime to 32 is 37

# Nearest prime to 163 is 167
print(nearest_prime_sum([50, 39, 49, 6, 17, 2]) == 4)