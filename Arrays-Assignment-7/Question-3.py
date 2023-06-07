# Given two non-negative integers, num1 and num2 represented as string, return *the sum of* num1 *and* num2 *as a string*.

# You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

# **Example 1:**

# **Input:** num1 = "11", num2 = "123"

# **Output:**

# "134"
def addStrings(num1, num2):
    result = []
    p1, p2 = len(num1) - 1, len(num2) - 1
    carry = 0

    while p1 >= 0 or p2 >= 0:
        d1 = int(num1[p1]) if p1 >= 0 else 0
        d2 = int(num2[p2]) if p2 >= 0 else 0

        total = d1 + d2 + carry
        digit = total % 10
        carry = total // 10

        result.insert(0, str(digit))

        p1 -= 1
        p2 -= 1

    if carry > 0:
        result.insert(0, str(carry))

    return ''.join(result)
num1 = int(input())
num2 = int(input())
print(addStrings(num1, num2))
