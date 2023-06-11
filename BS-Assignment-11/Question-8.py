# Given two integer arrays `nums1` and `nums2`, return *an array of their intersection*. Each element in the result must appear as many times as it shows in both arrays and you may return the result in **any order**.

# **Example 1:**
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]

# **Example 2:**
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.

from collections import defaultdict

def intersect(nums1, nums2):
    frequency = defaultdict(int)
    for num in nums1:
        frequency[num] += 1
    
    result = []
    for num in nums2:
        if frequency[num] > 0:
            result.append(num)
            frequency[num] -= 1
    
    return result

nums1=list(map(int,input().split()))
nums2=list(map(int,input().split()))
print(intersect(nums1,nums2))  

nums1=list(map(int,input().split()))
nums2=list(map(int,input().split()))
print(intersect(nums1,nums2))  
