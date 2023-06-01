# You are given an integer array nums and an integer k.

# In one operation, you can choose any index i where 0 <= i < nums.length and change nums[i] to nums[i] + x where x is an integer from the range [-k, k]. You can apply this operation at most once for each index i.

# The score of nums is the difference between the maximum and minimum elements in nums.

# Return the minimum score of nums after applying the mentioned operation at most once for each index in it.

# Example 1:
# Input: nums = [1], k = 0
# Output: 0

# Explanation: The score is max(nums) - min(nums) = 1 - 1 = 0.

def minimumScore(nums, k):
    min_val = min(nums)
    max_val = max(nums)

    if max_val - min_val <= 2 * k:
        return 0

    mid = (min_val + max_val) // 2

    for i in range(len(nums)):
        if nums[i] <= mid - k:
            nums[i] = mid - k
        elif nums[i] >= mid + k:
            nums[i] = mid + k

    new_min = min(nums)
    new_max = max(nums)

    return new_max - new_min

nums =list(map(int,input().split()))
k =  int(input())
print(minimumScore(nums, k))
