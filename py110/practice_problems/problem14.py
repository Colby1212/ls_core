# create a function that takes a single integer and returns the sum of all multiples of 7 or 11 that are less than the argument
# if a number is a multiple of 7 and both 11, count it once. 

# for example, the multipes of 7 and 11 that are below 25 are 7, 11, 14, 21. The sum is 75

# If the argument is negative return 0.

# examples
# print(seven_eleven(10) == 7)
# print(seven_eleven(11) == 7)
# print(seven_eleven(12) == 18)
# print(seven_eleven(25) == 75)
# print(seven_eleven(100) == 1153)
# print(seven_eleven(0) == 0)
# print(seven_eleven(-100) == 0)

# we can see here that it has to be below the number. So if it is a multiple of 7 or 11 it will not be included


# # Data types
# # integers, sum, list to keep track of numbers


# # Algorithm
# if a number is negative return 0
# iterate through every integer below negative
# if the number is divisible by 7 or 11 include it
# return the sum of all included numbers
# # Create 2 lists to keep track of multiples of 7 and 11
# # look for all multiples of 7 and 11 from 0 to the desired number
# # if it is a multiple of 7 and 11 we only count it once
# # add all the numbers together
# # return the sum

# Code

def seven_eleven(number):
    return sum(num for num in range(number) if num % 7 == 0 or num % 11 == 0)


print(seven_eleven(10) == 7)
print(seven_eleven(11) == 7)
print(seven_eleven(12) == 18)
print(seven_eleven(25) == 75)
print(seven_eleven(100) == 1153)
print(seven_eleven(0) == 0)
print(seven_eleven(-100) == 0)