# Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears **once** or **twice**, return *an array of all the integers that appears **twice***.

# You must write an algorithm that runs in O(n) time and uses only constant extra space.

# **Example 1:**

# **Input:** nums = [4,3,2,7,8,2,3,1]

# **Output:**[2,3]

def find_duplicates(nums):
    result = []
    for num in nums:
        index = abs(num) - 1
        if nums[index] < 0:
            result.append(abs(num))
        else:
            nums[index] *= -1
    return result

nums = list(map(int,input().split()))
result = find_duplicates(nums)
print(result)  
