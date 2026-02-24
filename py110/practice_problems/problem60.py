# problem
# create a function that takes a string of digits as an argument
# return the number of even-numbered substrings that can be formed
# If a substring occurs more than once it should count each occurence as a separate substring

# input --> list of numbers
# output --> integer

# examples and data types 

# print(even_substrings('1432') == 6)
# print(even_substrings('3145926') == 16)
# print(even_substrings('2718281') == 16)
# print(even_substrings('13579') == 0)
# print(even_substrings('143232') == 12)

# data types
# strings, integers

# Algorithm
# create a variable to keep track of the amount of even-numbered substrings that can be formed
# create a variable that contains the even numbers
# if the number is an even number add the length of that number to the variable to keep track of even numbered substrings
# return the variable

def even_substrings(number):
    count = 0
    evens = '02468'
    for idx in range(len(number)):
        if number[idx] in evens:
            count += len(number[:idx]) + 1
    return count 

print(even_substrings('1432') == 6)
print(even_substrings('3145926') == 16)
print(even_substrings('2718281') == 16)
print(even_substrings('13579') == 0)
print(even_substrings('143232') == 12)