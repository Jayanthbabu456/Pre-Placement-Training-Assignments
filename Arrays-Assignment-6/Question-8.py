# Given two [sparse matrices](https://en.wikipedia.org/wiki/Sparse_matrix) mat1 of size m x k and mat2 of size k x n, return the result of mat1 x mat2. You may assume that multiplication is always possible.

# **Example 1:**
# **Input:** mat1 = [[1,0,0],[-1,0,3]], mat2 = [[7,0,0],[0,0,0],[0,0,1]]

# **Output:**

# [[7,0,0],[-7,0,3]]

def multiply(mat1, mat2):
    m, k, n = len(mat1), len(mat1[0]), len(mat2[0])
    result = [[0] * n for _ in range(m)]

    for i in range(m):
        sparse_row = {}
        for j in range(k):
            if mat1[i][j] != 0:
                sparse_row[j] = mat1[i][j]

        for j in range(n):
            sparse_col = {}
            for k in range(k):
                if mat2[k][j] != 0:
                    sparse_col[k] = mat2[k][j]

            for k in sparse_row:
                if k in sparse_col:
                    result[i][j] += sparse_row[k] * sparse_col[k]

    return result

mat1 = [[1, 0, 0], [-1, 0, 3]]
mat2 = [[7, 0, 0], [0, 0, 0], [0, 0, 1]]
print(multiply(mat1, mat2))
