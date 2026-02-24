# write a function that takes a list of denominators of an ehyptian fraction and returns the rational number that represents it

# input -->  a list of denominators
# output --> a rational number

# examples and test cases
# Test Cases:
# print(unegyptian([1, 2, 3, 6]) == Fraction(2, 1))
# print(unegyptian([1, 2, 3, 4, 5]) == Fraction(137, 60))
# print(unegyptian([2, 3, 4, 5]) == Fraction(77, 60))
# print(unegyptian([1, 1, 1, 1]) == Fraction(4, 1))


# Data types:
# floats? lists

# algorithm
# Iterate over the list
# create a variable to represent the sum of all numbers in the list
# each number in the list is a denominator with a numerator of once
# Add each number to the created variable
# return the variable?


# Code:

from fractions import Fraction

def unegyptian(lst):
    return sum([Fraction(1, num) for num in lst])

print(unegyptian([1, 2, 3, 6]) == Fraction(2, 1))
print(unegyptian([1, 2, 3, 4, 5]) == Fraction(137, 60))
print(unegyptian([2, 3, 4, 5]) == Fraction(77, 60))
print(unegyptian([1, 1, 1, 1]) == Fraction(4, 1))
