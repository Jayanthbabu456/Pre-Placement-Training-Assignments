# Given an integer array nums of length n and an integer target, find three integers
# in nums such that the sum is closest to the target.
# Return the sum of the three integers.

# You may assume that each input would have exactly one solution.

# Example 1:
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2

# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

def threeSumClosest(nums, target):
    nums.sort()  

    n = len(nums)
    closestSum = float('inf')  

    for i in range(n - 2):  
        left = i + 1
        right = n - 1

        while left < right: 
            currentSum = nums[i] + nums[left] + nums[right]

            if abs(currentSum - target) < abs(closestSum - target):  
                closestSum = currentSum

            if currentSum < target:  
                left += 1
            elif currentSum > target:  
                right -= 1
            else:  
                return currentSum

    return closestSum  
nums = list(map(int,input().split()))
target = int(input())
result = threeSumClosest(nums, target)
print(result)
