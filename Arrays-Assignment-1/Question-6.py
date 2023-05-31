# Q6. Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:
# Input: nums = [1,2,3,1]

# Output: true




def contains_duplicate(nums):
    return len(nums) != len(set(nums))
nums = list(map(int,input().split()))
result = contains_duplicate(nums)
print(result)
