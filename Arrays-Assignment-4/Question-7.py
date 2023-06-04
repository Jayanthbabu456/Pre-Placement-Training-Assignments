#  You are given an m x n matrix M initialized with all 0's and an array of operations ops, where ops[i] = [ai, bi] means M[x][y] should be incremented by one for all 0 <= x < ai and 0 <= y < bi.

# Count and return *the number of maximum integers in the matrix after performing all the operations*

# **Example 1:**

# **Input:** m = 3, n = 3, ops = [[2,2],[3,3]]

# **Output:** 4

# **Explanation:** The maximum integer in M is 2, and there are four of it in M. So return 4.

def max_count(m, n, ops):
    min_ai = m
    min_bi = n

    for ai, bi in ops:
        min_ai = min(min_ai, ai)
        min_bi = min(min_bi, bi)

    return min_ai * min_bi

m = int(input())
n = int(input())
ops = []
num_ops = int(input())
for _ in range(num_ops):
    ai, bi = map(int, input().split())
    ops.append([ai, bi])
result = max_count(m, n, ops)
print(result)  
