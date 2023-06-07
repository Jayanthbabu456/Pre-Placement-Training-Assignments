# You are given an m x n integer matrix matrix with the following two properties:

# - Each row is sorted in non-decreasing order.
# - The first integer of each row is greater than the last integer of the previous row.

# Given an integer target, return true *if* target *is in* matrix *or* false *otherwise*.

# You must write a solution in O(log(m * n)) time complexity.

# **Example 1:**

# **Input:** matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3

# **Output:** true

def searchMatrix(matrix, target):
    m = len(matrix)
    n = len(matrix[0]) if m > 0 else 0
    left = 0
    right = m * n - 1

    while left <= right:
        mid = (left + right) // 2
        row = mid // n
        col = mid % n
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


m = int(input())
n = int(input())

matrix = []
for i in range(m):
    row = list(map(int, input().split()))
    matrix.append(row)

target = int(input())


result = searchMatrix(matrix, target)
print(result)
