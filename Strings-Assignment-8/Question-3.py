# Given two strings word1 and word2, return *the minimum number of **steps** required to make* word1 *and* word2 *the same*.

# In one **step**, you can delete exactly one character in either string.

# **Example 1:**

# **Input:** word1 = "sea", word2 = "eat"

# **Output:** 2

# **Explanation:** You need one step to make "sea" to "ea" and another step to make "eat" to "ea".

def minSteps(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0] * (n+1) for _ in range(m+1)]

   
    for i in range(1, m+1):
        dp[i][0] = dp[i-1][0] + 1
    for j in range(1, n+1):
        dp[0][j] = dp[0][j-1] + 1

    
    for i in range(1, m+1):
        for j in range(1, n+1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1)

    return dp[m][n]

word1 = input()
word2 = input()
result = minSteps(word1, word2)
print(result)  
