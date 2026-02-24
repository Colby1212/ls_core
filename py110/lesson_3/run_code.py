# def transpose(matrix):
#     transposed = []
#     new_rows_count = len(matrix[0])
    
#     for _ in range(new_rows_count):
#         transposed.append([])
        
        
#     for row_idx in range(len(matrix)):
#         for col_idx in range(len(matrix[row_idx])):
#             transposed[col_idx].append(matrix[row_idx][col_idx])
#     return transposed
def transpose(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    return [[matrix[r][c] for r in range(rows)] for c in range(columns)]
    
matrix2 = [
    [3, 7, 4, 2],
    [5, 1, 0, 8],
]

print(transpose(matrix2))