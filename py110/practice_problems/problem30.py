# Write a function that takes a nested list of lists(matrix)
# and returns the transpose of the matrix. 

# What is transpose? --> columns become the rows and rows become the columns

# input --> Nested list of lists
# output --> new list of lists that is the transposed version of the input matrix

# can we assume that the lengths of each nested list are the same? yes

# examples:

# Test Cases:
# matrix = [
#  [1, 5, 8],
#  [4, 7, 2],
#  [3, 9, 6]
# ]


# new_matrix = transpose(matrix)


# print(new_matrix == [[1, 4, 3], [5, 7, 9], [8, 2, 6]])
# print(matrix == [[1, 5, 8], [4, 7, 2], [3, 9, 6]])

# data types:
# lists, integers, nested lists


# Algorithm:
# create an empty list to hold the new transposed matrix
# iterate through the items of the list and grab the first index of each nested list
# append those items into a new list in the new matrix
# repeat this for each item in the nested lists. 
# return the new list


# # Code:


# def transpose(matrix):
#     transposed = []
#     for idx in range(len(matrix[0])):
#         new_line = []
#         for row in matrix:
#             new_line.append(row[idx])
#         transposed.append(new_line)
#     print(transposed)
#     return transposed


# matrix = [
#  [1, 5, 8],
#  [4, 7, 2],
#  [3, 9, 6]
# ]


# new_matrix = transpose(matrix)


# print(new_matrix == [[1, 4, 3], [5, 7, 9], [8, 2, 6]])
# print(matrix == [[1, 5, 8], [4, 7, 2], [3, 9, 6]])

# def transpose(matrix):
#     row = len(matrix)
#     column = len(matrix[0])
#     return [[matrix[r][c] for r in range(rows)] for c in range(columns)]

# matrix = [
#  [1, 5, 8],
#  [4, 7, 2],
#  [3, 9, 6]
# ]


# new_matrix = transpose(matrix)


# print(new_matrix == [[1, 4, 3], [5, 7, 9], [8, 2, 6]])
# print(matrix == [[1, 5, 8], [4, 7, 2], [3, 9, 6]])

def transpose(matrix):
    return [list(col) for col in zip(*matrix)]

matrix = [
 [1, 5, 8],
 [4, 7, 2],
 [3, 9, 6]
]


new_matrix = transpose(matrix)


print(new_matrix == [[1, 4, 3], [5, 7, 9], [8, 2, 6]])
print(matrix == [[1, 5, 8], [4, 7, 2], [3, 9, 6]])