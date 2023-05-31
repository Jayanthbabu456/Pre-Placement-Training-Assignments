
# Q1.Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Example:
# Input: nums = [2,7,11,15], target = 9
# Output0 [0,1]

# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]


def find_two_sum(nums, target):
    nums_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in nums_dict:
            return [nums_dict[complement], i]
        nums_dict[num] = i
    return []


nums = list(map(int,input().split()))
target =int(input())
result = find_two_sum(nums, target)
print(result)
