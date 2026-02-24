# create a function that takes a string argument that consists of numeric digits
# compute the greatest product of four consecutive digits in the string
# The argument will always have more than 4 digits
# Input --> string of integers
# output --> largest product of 4 consecutive digits

# explicit --> THERE WILL ALWAYS BE 4 digits


# Examples

# print(greatest_product('23456') == 360)      # 3 * 4 * 5 * 6
# print(greatest_product('3145926') == 540)    # 5 * 9 * 2 * 6
# print(greatest_product('1828172') == 128)    # 1 * 8 * 2 * 8
# print(greatest_product('123987654') == 3024) # 9 * 8 * 7 * 6

# Data types

# integers, strings, collection?


# Algorithm
# create a counter to track the largest product
# check the string 4 consecutive items at a time and find their product
# amongst the products, return the largest one. 

# Code

def greatest_product(numbers):
    largest_product = 0
    for idx in range(len(numbers) - 3):
        current_product = 1
        for num in numbers[idx: idx+4]:
            current_product *= int(num)
        largest_product = max(largest_product, current_product)
    return largest_product


print(greatest_product('23456') == 360)      # 3 * 4 * 5 * 6
print(greatest_product('3145926') == 540)    # 5 * 9 * 2 * 6
print(greatest_product('1828172') == 128)    # 1 * 8 * 2 * 8
print(greatest_product('123987654') == 3024) # 9 * 8 * 7 * 6