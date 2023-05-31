# Q7.Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the nonzero elements.

# Note that you must do this in-place without making a copy of the array.

# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]



def move_zeroes(nums):
    j = 0  

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[j] = nums[j], nums[i]   
            j += 1

   
    nums[j:] = [0] * (len(nums) - j)

    return nums
nums =list(map(int,input().split()))
result = move_zeroes(nums)
print(result)
