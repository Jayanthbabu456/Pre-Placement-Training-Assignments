# Given two strings s and p, return *an array of all the start indices of* p*'s anagrams in* s. You may return the answer in **any order**.

# An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# **Example 1:**

# **Input:** s = "cbaebabacd", p = "abc"

# **Output:** [0,6]

# **Explanation:**

# The substring with start index = 0 is "cba", which is an anagram of "abc".

# The substring with start index = 6 is "bac", which is an anagram of "abc".

from collections import Counter

def findAnagrams(s, p):
    pCount = Counter(p)
    left = right = matchCount = 0
    result = []

    while right < len(s):
        
        pCount[s[right]] -= 1
        right += 1

        if pCount[s[right - 1]] == 0:
            matchCount += 1

       
        if matchCount == len(pCount):
            result.append(left)

       
        if right - left == len(p):
            pCount[s[left]] += 1

            if pCount[s[left]] == 1:
                matchCount -= 1
           
            left += 1

    return result

s = input()
p = input()
result = findAnagrams(s, p)
print(result)  
