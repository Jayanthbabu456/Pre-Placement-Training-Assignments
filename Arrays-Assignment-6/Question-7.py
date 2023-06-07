# Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

# **Example 1:**
# **Input:** n = 3

# **Output:** [[1,2,3],[8,9,4],[7,6,5]]

def generateMatrix(n):
    result = [[0] * n for _ in range(n)]
    top, bottom, left, right = 0, n - 1, 0, n - 1
    num = 1

    while num <= n * n:
        
        for i in range(left, right + 1):
            result[top][i] = num
            num += 1
        top += 1

       
        for i in range(top, bottom + 1):
            result[i][right] = num
            num += 1
        right -= 1

      
        for i in range(right, left - 1, -1):
            result[bottom][i] = num
            num += 1
        bottom -= 1

       
        for i in range(bottom, top - 1, -1):
            result[i][left] = num
            num += 1
        left += 1

    return result
n = int(input())
print(generateMatrix(n))
