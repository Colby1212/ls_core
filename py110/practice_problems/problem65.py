# create a function that takes a string argument that consists of number digits
# compute the greatest product of four consecutive digits in the string 
# rules:

# inputs will always have more than 4 digits

# input --> string of integers
# output --> greatest product of 4 conseuctive integers in the string


# examples and test cases 

# print(greatest_product('23456') == 360)      # 3 * 4 * 5 * 6
# print(greatest_product('3145926') == 540)    # 5 * 9 * 2 * 6
# print(greatest_product('1828172') == 128)    # 1 * 8 * 2 * 8
# print(greatest_product('123987654') == 3024) # 9 * 8 * 7 * 6

# they will always be positive because the string consists of entirely numeric digits

# data types

# string, collections integers


# Algorithm

# Iterate over the list fourr digits at a time up until the fourth last character
# find the product of each of these groups
# return the largest product 



# Code

def greatest_product(string_numbers):
    products = []

    for first_index in range(len(string_numbers) - 3):
        current_product = 1
        last_index = first_index + 4

        for num in string_numbers[first_index:last_index]:

            current_product *= int(num)
        products.append(current_product)
    return max(products)

print(greatest_product('23456') == 360)      # 3 * 4 * 5 * 6
print(greatest_product('3145926') == 540)    # 5 * 9 * 2 * 6
print(greatest_product('1828172') == 128)    # 1 * 8 * 2 * 8
print(greatest_product('123987654') == 3024) # 9 * 8 * 7 * 6
