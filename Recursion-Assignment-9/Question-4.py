# Given a number N and a power P, the task is to find the exponent of this number raised to the given power, i.e. N^P.

# **Example 1 :** 

# Input: N = 5, P = 2

# Output: 25

# **Example 2 :**
# Input: N = 2, P = 5

# Output: 32

def calculateExponent(N, P):
    result = N ** P
    return result


N = int(input())
P = int(input())
result = calculateExponent(N, P)
print(result) 

N = int(input())
P = int(input())
result = calculateExponent(N, P)
print(result)
