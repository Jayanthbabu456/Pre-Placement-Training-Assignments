# Given two strings s and t, return true *if they are equal when both are typed into empty text editors*. '#' means a backspace character.

# Note that after backspacing an empty text, the text will continue empty.

# **Example 1:**

# **Input:** s = "ab#c", t = "ad#c"

# **Output:** true

# **Explanation:**

# Both s and t become "ac".

def backspaceCompare(s, t):
    def processString(string):
        result = []
        for c in string:
            if c != '#':
                result.append(c)
            elif result:
                result.pop()
        return ''.join(result)

    processed_s = processString(s)
    processed_t = processString(t)

    return processed_s == processed_t
s = input()
t = input()
print(backspaceCompare(s, t))
