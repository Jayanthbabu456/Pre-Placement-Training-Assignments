# Given a positive integer, N. Find the factorial of N. 

# **Example 1:**

# Input: N = 5 

# Output: 120

# **Example 2:**

# Input: N = 4

# Output: 24

def factorial(N):
    factorial = 1
    for i in range(1, N+1):
        factorial *= i
    return factorial


N = int(input())
result = factorial(N)
print(result)  

N = int(input())
result = factorial(N)
print(result)
