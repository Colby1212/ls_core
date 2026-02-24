# Write a function that takes an arbritraty MxN matrix, rotates it 90 degrees clockwise, and returns the result as a new matrix


# input --> matrix
# output --> new matrix rotated 90 degrees clockwise

# Write a function
# that takes a list of lists as an input
# rotate the matrix 90 degrees to the right, 
# output the new matrix

# Questions
# what is a matrix? 
# What does rotating it 90 degrees mean?


# Examples / test cases 

# matrix1 = [
#   [1, 5, 8],
#   [4, 7, 2],
#   [3, 9, 6],
# ]




# rotated_2 = [
#     [5, 3],
#     [1, 7],
#     [0, 4]
#     [8, 2],
# ]

# new_matrix1 = rotate90(matrix1)
# new_matrix2 = rotate90(matrix2)
# new_matrix3 = rotate90(rotate90(rotate90(rotate90(matrix2))))


# print(new_matrix1 == [[3, 4, 1], [9, 7, 5], [6, 2, 8]])
# print(new_matrix2 == [[5, 3], [1, 7], [0, 4], [8, 2]])
# print(new_matrix3 == new_matrix2)


# data types

# lists, integers

# algorithm

# Create a new list 
# The length of the rows are going to be the amount of columns in the matrix
# and the amount of columns are going to be the length of each row of the original matrix
# Because we are looking to rotate it clockwise, the first number of each row will correspond with the 
# numbers in the last row of the original list. the second will correspond with the second last, and so forth.
# Essentially the new rows will be the original matrix's columns counting upwards from the bottom!

# 1. Create a new list
# 2. Iterate over each row of the list starting from the bottom
# 3. Take the first number of each row and add it to a new list
# 4. Take that new list and add it to the empty list
# 5. Now repeat steps 2-4 For each number in the row. (first time was the first, second would be the second, etc. )
# 6. Return the new matrix (list of lists)


def rotate90(numbers):
    new_matrix = []
    for idx in range(len(numbers[0])):
        new_row = []
        for num in range(len(numbers) -1, -1, -1):
            new_row.append(numbers[num][idx])
        new_matrix.append(new_row)
    return new_matrix


def rotate90(numbers):
    return [[numbers[num][idx] for num in reversed(range(len(numbers)))] 
                               for idx in range(len(numbers[0]))]

matrix1 = [
  [1, 5, 8],
  [4, 7, 2],
  [3, 9, 6],
]

new_matrix1 = rotate90(matrix1)

print(new_matrix1 == [[3, 4, 1], [9, 7, 5], [6, 2, 8]])

matrix2 = [
  [3, 7, 4, 2],
  [5, 1, 0, 8],
]

new_matrix2 = rotate90(matrix2)

print(new_matrix2 == [[5, 3], [1, 7], [0, 4], [8, 2]])