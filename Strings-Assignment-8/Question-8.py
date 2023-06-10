# Given two strings s and goal, return true *if you can swap two letters in* s *so the result is equal to* goal*, otherwise, return* false*.*

# Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at s[i] and s[j].

# - For example, swapping at indices 0 and 2 in "abcd" results in "cbad".

# **Example 1:**

# **Input:** s = "ab", goal = "ba"

# **Output:** true

# **Explanation:** You can swap s[0] = 'a' and s[1] = 'b' to get "ba", which is equal to goal.

def Strings(s, goal):
    if len(s) != len(goal):
        return False

    diff = []
    for i in range(len(s)):
        if s[i] != goal[i]:
            diff.append(i)

    if len(diff) != 2:
        return False

    if s[diff[0]] == goal[diff[1]] and s[diff[1]] == goal[diff[0]]:
        return True

    return False


s = input()
goal = input()
result = Strings(s, goal)
print(result)  
