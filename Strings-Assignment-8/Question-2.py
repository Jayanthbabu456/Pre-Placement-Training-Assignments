# Given a string s containing only three types of characters: '(', ')' and '*', return true *if* s *is **valid***.

# The following rules define a **valid** string:

# - Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# - Any right parenthesis ')' must have a corresponding left parenthesis '('.
# - Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# - '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".

# **Example 1:**

# **Input:** s = "()"

# **Output:**

# true

def checkValidString(s):
    stack = []
    star_stack = []

    for c in s:
        if c == '(':
            stack.append(c)
        elif c == '*':
            star_stack.append(c)
        elif c == ')':
            if stack:
                stack.pop()
            elif star_stack:
                star_stack.pop()
            else:
                return False

    while stack and star_stack:
        if stack[-1] > star_stack[-1]:
            return False
        stack.pop()
        star_stack.pop()

    return len(stack) == 0

s = input()
result = checkValidString(s)
print(result)  
