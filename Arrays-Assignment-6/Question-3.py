# Given an array of integers arr, return *true if and only if it is a valid mountain array*.

# Recall that arr is a mountain array if and only if:

# - arr.length >= 3
# - There exists some i with 0 < i < arr.length - 1 such that:
#     - arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
#     - arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# **Example 1:**

# **Input:** arr = [2,1]

# **Output:**

# false

def validMountainArray(arr):
    n = len(arr)
    if n < 3:
        return False

    left = 0
    right = n - 1

    while left < right:
        if arr[left] < arr[left + 1]:
            left += 1
        elif arr[right] < arr[right - 1]:
            right -= 1
        else:
            break

    return left == right


arr = list(map(int,input().split()))
print(validMountainArray(arr))
