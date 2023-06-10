# Given an integer `n`, return *`true` if it is a power of two. Otherwise, return `false`*.

# An integer `n` is a power of two, if there exists an integer `x` such that `n == 2x`.

# **Example 1:**
# Input: n = 1 

# Output: true

# **Example 2:**
# Input: n = 16 

# Output: true

# **Example 3:**
# Input: n = 3 

# Output: false

def isPowerOfTwo(n):
    if n <= 0:
        return False
    return (n & (n - 1)) == 0


n = int(input())
result = isPowerOfTwo(n)
print(result)  

n = int(input()) 
result = isPowerOfTwo(n)
print(result)  

n = int(input())
result = isPowerOfTwo(n)
print(result)  
