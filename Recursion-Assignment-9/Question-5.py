# Given an array of integers **arr**, the task is to find maximum element of that array using recursion.

# **Example 1:**

# Input: arr = {1, 4, 3, -5, -4, 8, 6};
# Output: 8

# **Example 2:**

# Input: arr = {1, 4, 45, 6, 10, -8};
# Output: 45

def findMax(arr, start, end):
    if start == end:
        return arr[start]

    mid = (start + end) // 2
    maxLeft = findMax(arr, start, mid)
    maxRight = findMax(arr, mid + 1, end)

    return max(maxLeft, maxRight)


arr = list(map(int,input().split()))
result = findMax(arr, 0, len(arr) - 1)
print(result)  

arr = list(map(int,input().split()))
result = findMax(arr, 0, len(arr) - 1)
print(result) 
