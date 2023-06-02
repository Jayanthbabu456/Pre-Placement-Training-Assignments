# Given an array nums of n integers, return an array of all the unique quadruplets
# [nums[a], nums[b], nums[c], nums[d]] such that:
#            ● 0 <= a, b, c, d < n
#            ● a, b, c, and d are distinct.
#            ● nums[a] + nums[b] + nums[c] + nums[d] == target

# You may return the answer in any order.

# Example 1:
# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

def fourSum(nums, target):
    nums.sort()  

    n = len(nums)
    result = []  

    for i in range(n - 3):  
        if i > 0 and nums[i] == nums[i - 1]:
            continue  

        for j in range(i + 1, n - 2):  
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue  

            left = j + 1
            right = n - 1

            while left < right:  
                currentSum = nums[i] + nums[j] + nums[left] + nums[right]

                if currentSum == target:  
                    result.append([nums[i], nums[j], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif currentSum < target:  
                    left += 1
                else:  
                    right -= 1

    return result  

nums = list(map(int,input().split()))
target = int(input())
result = fourSum(nums, target)
print(result)
