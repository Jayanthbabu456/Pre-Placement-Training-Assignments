# Given a non-empty array of integers nums, every element appears twice except
# for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only
# constant extra space.

# Example 1:
# Input: nums = [2,2,1]
# Output: 1

def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

nums = list(map(int,input().split()))
result = singleNumber(nums)
print(result)
