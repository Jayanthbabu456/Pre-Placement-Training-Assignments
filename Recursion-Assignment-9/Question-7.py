# Given a string S, the task is to write a program to print all permutations of a given string.

# **Example 1:**

# ***Input:***

# *S = “ABC”*

# ***Output:***

# *“ABC”, “ACB”, “BAC”, “BCA”, “CBA”, “CAB”*

# **Example 2:**

# ***Input:***

# *S = “XY”*

# ***Output:***

# *“XY”, “YX”*

def permute(s, l, r):
    if l == r:
        print("".join(s))
    else:
        for i in range(l, r + 1):
            s[l], s[i] = s[i], s[l]
            permute(s, l + 1, r)
            s[l], s[i] = s[i], s[l]  


S = input()
permute(list(S))

S = input() 
permute(list(S))
