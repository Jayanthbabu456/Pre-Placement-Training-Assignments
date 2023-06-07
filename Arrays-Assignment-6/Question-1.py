# A permutation perm of n + 1 integers of all the integers in the range [0, n] can be represented as a string s of length n where:

# - s[i] == 'I' if perm[i] < perm[i + 1], and
# - s[i] == 'D' if perm[i] > perm[i + 1].

# Given a string s, reconstruct the permutation perm and return it. If there are multiple valid permutations perm, return **any of them**.

# **Example 1:**

# **Input:** s = "IDID"

# **Output:**

# [0,4,1,3,2]

def reconstruct_permutation(s):
    n = len(s)
    perm = []
    start = 0
    end = 0

    for i in range(n):
        if s[i] == 'I':
            perm.append(start)
            start += 1
        else:
            perm.append(end)
            end -= 1

    perm.append(start)  
    return perm

s = "IDID"
print(reconstruct_permutation(s))
