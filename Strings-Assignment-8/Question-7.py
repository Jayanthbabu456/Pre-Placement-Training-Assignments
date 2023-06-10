# Given an encoded string, return its decoded string.

# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

# You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

# The test cases are generated so that the length of the output will never exceed 105.

# **Example 1:**

# **Input:** s = "3[a]2[bc]"

# **Output:** "aaabcbc"

def decodeString(s):
    stack = []

    for c in s:
        if c.isdigit():
            num = 0
            while c.isdigit():
                num = num * 10 + int(c)
                c = s.pop(0)
            stack.append(num)

        if c == '[':
            stack.append(c)

        if c == ']':
            decodedStr = ''
            while stack[-1] != '[':
                decodedStr = stack.pop() + decodedStr
            stack.pop()  

            k = stack.pop()  
            decodedStr = decodedStr * k
            stack.append(decodedStr)

    return ''.join(stack[::-1])


s = input()
result = decodeString(s)
print(result)  
