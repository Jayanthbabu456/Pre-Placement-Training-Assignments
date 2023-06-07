# Given a binary array nums, return *the maximum length of a contiguous subarray with an equal number of* 0 *and* 1.

# **Example 1:**

# **Input:** nums = [0,1]

# **Output:** 2

# **Explanation:**

# [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.

def findMaxLength(nums):
    sum_map = {0: -1}  
    max_len = 0
    running_sum = 0

    for i in range(len(nums)):
        running_sum += 1 if nums[i] == 1 else -1

        if running_sum in sum_map:
            max_len = max(max_len, i - sum_map[running_sum])
        else:
            sum_map[running_sum] = i

    return max_len

nums = list(map(int,input().split()))
print(findMaxLength(nums))
