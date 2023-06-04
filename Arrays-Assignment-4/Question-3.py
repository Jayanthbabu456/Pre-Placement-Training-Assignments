# Given a 2D integer array matrix, return *the **transpose** of* matrix.

# The **transpose** of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

# **Example 1:**

# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]

# Output: [[1,4,7],[2,5,8],[3,6,9]]

def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    transposed_matrix = [[0] * rows for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            transposed_matrix[j][i] = matrix[i][j]

    return transposed_matrix
matrix = []
line = input()
elements = line.split(',')
for element in elements:
    row = [int(num) for num in element.split()]
    matrix.append(row)

result = transpose(matrix)
print(result)  
