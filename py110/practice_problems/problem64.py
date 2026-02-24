# create a function that takes a single integer

# return the sum of all the multiples of 7 or 11 that are less than the argument
# If a number is a multiple of both 7 and 11 count, it just occruance


# for example the multiples of 7 and 11 that are below 7, 11, 14, 21 the sum of these multiples is 75

# If the argument is negative return 0



# examples, and data types 

# print(seven_eleven(10) == 7)
# print(seven_eleven(11) == 7)
# print(seven_eleven(12) == 18)
# print(seven_eleven(25) == 75)
# print(seven_eleven(100) == 1153)
# print(seven_eleven(0) == 0)
# print(seven_eleven(-100) == 0)

# doesnt include the number, just numbers below it
# 0 and negative return 0



# Data types

# Collections, integers


# Algorithm

# Check to see if the number is less than 8, anything less than 8 should return 0

# find all unique numbers that are multiples of 7 or 11 that are below the number

# Sum the numbers

# return the sum


# Code 


def seven_eleven(number):
    if number < 8:
        return 0
    return sum(set(num for num in range(number) if num % 7 == 0 or num % 11 == 0))

print(seven_eleven(10) == 7)
print(seven_eleven(11) == 7)
print(seven_eleven(12) == 18)
print(seven_eleven(25) == 75)
print(seven_eleven(100) == 1153)
print(seven_eleven(0) == 0)
print(seven_eleven(-100) == 0)
