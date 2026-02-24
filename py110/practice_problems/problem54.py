# create a function that takes a list of integers as an argument and returns a tuple of two numbers that are closest together in value
# If there are multiple pairs that are equally close, return the pair that occurs first in the list

# input --> list of numbers
# output --> tuple of two numbers that are closests in value

# examples and data types 

# print(closest_numbers([5, 25, 15, 11, 20]) == (15, 11))
# print(closest_numbers([19, 25, 32, 4, 27, 16]) == (25, 27))
# print(closest_numbers([12, 22, 7, 17]) == (12, 7))



# They are two numbers that are closest in value, does not have to be consecutive numbers

# Data types
# tuples, integers, lists 

# Algorithm

# Create a tuple that contains the first two elements of the list
# create a variable to keep track of the current lowest difference between values
# iterate over each number in the list
# for each number compare it with the other numbers individually
# if the difference is lower than the current difference, change the value of the variable keeping track
# also make it so that the two numbers being compared are the two in the tuple
# Repeat until we finish iterating over the numbers
# return the tuple

def closest_numbers(numbers):
    closest_value = abs(numbers[0] - numbers[1])
    closest = (numbers[0], numbers[1])
    for index in range(len(numbers) -1):
        num1 = numbers[index]
        for num2 in numbers[index+1:]:
            current_value = abs(num1 - num2)
            if current_value < closest_value:
                closest = (num1, num2)
                closest_value = current_value
    return closest


print(closest_numbers([5, 25, 15, 11, 20]) == (15, 11))
print(closest_numbers([19, 25, 32, 4, 27, 16]) == (25, 27))
print(closest_numbers([12, 22, 7, 17]) == (12, 7))
