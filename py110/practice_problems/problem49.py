# write a function that takes a positive integer as an argument and returns the difference between
# the square of teh sum of the first n positive integers and teh sum of the squares of the first n positive integers

# input --> num

# output --> Integer?


# examples and test cases 

# Test Cases:
# print(sum_square_difference(3) == 22)      # (1 + 2 + 3)**2 - (1**2 + 2**2 + 3**2)
# print(sum_square_difference(10) == 2640)
# print(sum_square_difference(1) == 0)
# print(sum_square_difference(100) == 25164150)
# ***



# num1 -->  1 + 2 + 3 all squares
# num2 --> sum of 1^2, 2^2, 3^3
# returns the difference


# data types

# integers


# algorithm
# Create two variables
# 1 for the sum of all positive integers leading to the number
# 2 for the sum of all squares of positive integers leading to the number

# Iterate through all the n positive numbers 
# for each number add the value to the first variable, and then square the number and add it to the second


def sum_square_difference(num):
    sum_of_nums = 0
    sum_squares = 0
    for integer in range(num+1):
        sum_of_nums += integer
        sum_of_squares += integer **2
    return (sum_of_nums**2) - sum_squares

print(sum_square_difference(3) == 22)      # (1 + 2 + 3)**2 - (1**2 + 2**2 + 3**2)
print(sum_square_difference(10) == 2640)
print(sum_square_difference(1) == 0)
print(sum_square_difference(100) == 25164150)

def sum_square_difference(n):
    return sum(range(1, n + 1)) ** 2 - sum(i * i for i in range(1, n + 1))


def sumsquare_difference(n):
    return sum(range(1, n +1)) **2 - sum(i*I for i in range(1, n+1))