# We define a harmonious array as an array where the difference between its maximum value
# and its minimum value is exactly 1.

# Given an integer array nums, return the length of its longest harmonious subsequence
# among all its possible subsequences.

# A subsequence of an array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.

# Example 1:
# Input: nums = [1,3,2,2,5,2,3,7]
# Output: 5

# Explanation: The longest harmonious subsequence is [3,2,2,2,3].

def findLHS(nums):
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1

    max_length = 0
    for num in count:
        if num + 1 in count:
            length = count[num] + count[num + 1]
            max_length = max(max_length, length)

    return max_length

nums = list(map(int,input().split()))
print(findLHS(nums))
