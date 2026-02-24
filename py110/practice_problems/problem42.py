# Egyptian fractions

# The sum of a series of distinct unit fractions (fractions witha  numerator of 1)
# In general any positive rational number can be expressed as an egyptian fraction
# Write a function that takes a rational number as an argument and returns a list of the denominators of an egyptan fraction representation f the number

# input --> a rational number, 2 numbers
# output --> a list of denominators of an egyptian fraction 

# Rules --> a denominator can only be used once, and the numereator must always be 10 

# examples / test cases Test Cases:
# print(egyptian(Fraction(2, 1)) == [1, 2, 3, 6])
# print(egyptian(Fraction(137, 60)) == [1, 2, 3, 4, 5])
# print(egyptian(Fraction(3, 1)) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
#                                    15, 230, 57960])


# for the first test case we see 

# 2/1 (2) == 1/1 + 1/2 + 1/3 + 1/6

# 1/1 = 1
# 1/2  = 0.5
# 1/3 + 1/6 = 0.5

# data types:
# floats? fractions, lists

# algorithm

# create a variable for the numerator, set the numerator to 1
# create a variable for the denominator, set the numerator to 1
# create a variable that represents the original number
# if the numerator divided by the denominator is less than or equal to the number, substract it from the origianl number
# if it is not do not subtract it
# add 1 to the denominator and repeat
# do so until the original number is reduced to 0 
# keep doing so until the number is reduced to 0 

# code
from fractions import Fraction

def egyptian(num):
    denominator = 1
    denominator_lst = []
    while num > 0:
        unit = Fraction(1, denominator)
        if num >= egyptian_num:
            num -= egyptian_num
            denominator_lst.append(denominator)
        denominator += 1
    return denominator_lst


print(egyptian(Fraction(2, 1)) == [1, 2, 3, 6])
print(egyptian(Fraction(137, 60)) == [1, 2, 3, 4, 5])
print(egyptian(Fraction(3, 1)) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                                   15, 230, 57960])