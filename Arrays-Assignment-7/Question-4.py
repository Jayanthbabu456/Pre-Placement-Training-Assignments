# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

# **Example 1:**

# **Input:** s = "Let's take LeetCode contest"

# **Output:** "s'teL ekat edoCteeL tsetnoc"

def reverseWords(s):
    words = s.split()
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)
s = input()
print(reverseWords(s))
