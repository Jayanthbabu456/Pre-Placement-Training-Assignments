# Given two strings s and t, *determine if they are isomorphic*.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

# **Example 1:**

# **Input:** s = "egg", t = "add"

# **Output:** true

def is_isomorphic(s, t):
    if len(s) != len(t):
        return False

    s_to_t = {}
    t_to_s = {}

    for i in range(len(s)):
        if s[i] not in s_to_t and t[i] not in t_to_s:
            s_to_t[s[i]] = t[i]
            t_to_s[t[i]] = s[i]
        elif s_to_t.get(s[i]) != t[i] or t_to_s.get(t[i]) != s[i]:
            return False

    return True
s = input()
t = input()
print(is_isomorphic(s, t))
