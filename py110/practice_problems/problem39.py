# a valid triangle is one where the sum of the lengths of the two shortest sides is greater than the length of the longest side, and every side has a length greater than 0
# Write a function that takes the length of the three sides of a triangle as an argument
# and returns one of the following four 'equilateral', 'isosceles', 'scalene', or 'invalid'.

# equilateral --> All sides are equal
# isoceles --> 2 sides are equal
# scalene --> no sides are equal
# invalid --> Not a valid triangle
# What is a valiid triangle?
# 3 sides
# len longest side < side1  + side 2 


# input --> 3 integers
# output --> one of four options 'equilateral', 'isosceles', 'scalene', or 'invalid'.

# Examples and test cases 

# print(triangle(3, 3, 3) == "equilateral")
# print(triangle(3, 3, 1.5) == "isosceles")
# print(triangle(3, 4, 5) == "scalene")
# print(triangle(0, 3, 3) == "invalid")
# print(triangle(3, 1, 1) == "invalid")

# All sides have to be greater than 0
# The sum of sides 1 and 2 have to be greater than side 3

# data types:

# strings and integers

# Algorithm

# Order the sides in ascending Order
# check to see if it is a valid triangle 
# All sides greater than 0 and the sum of the two shortest sides are longer than the longest side
# IF it is an invalid triangle return invalid
# Check to see how many different lengths there are
# return the type of triangle accordingly 


def triangle(side1, side2, side3):
    sides = sorted([side1, side2, side3])
    if (sides[0] + sides[1] <= sides[2]) or sides[0] <= 0:
        return 'invalid'
    uniqe_sides = len(set(sides))
    if unique_sides == 1:
        return 'equilateral'
    elif unique_sides == 2:
        return 'isosceles'
    else:
        return 'scalene'
    
print(triangle(3, 3, 3) == "equilateral")
print(triangle(3, 3, 1.5) == "isosceles")
print(triangle(3, 4, 5) == "scalene")
print(triangle(0, 3, 3) == "invalid")
print(triangle(3, 1, 1) == "invalid")