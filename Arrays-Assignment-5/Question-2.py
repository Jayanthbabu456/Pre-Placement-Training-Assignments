# You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase **may be** incomplete.

# Given the integer n, return *the number of **complete rows** of the staircase you will build*.

# **Example 1:**
# **Input:** n = 5

# **Output:** 2

# **Explanation:** Because the 3rd row is incomplete, we return 2.

def count_complete_rows(n):
    k = 0
    while (k * (k + 1)) // 2 <= n:
        k += 1
    return k - 1
n = int(input())
result = count_complete_rows(n)
print(result) 
