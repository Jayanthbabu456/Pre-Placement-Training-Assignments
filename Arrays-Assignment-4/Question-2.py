# Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

# - answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
# - answer[1] is a list of all distinct integers in nums2 which are not present in nums1.

# Note that the integers in the lists may be returned in any order.
# Example 1:
# Input:nums1 = [1,2,3], nums2 = [2,4,6]
# Output:[[1,3],[4,6]]
# Explanation:

# For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1 and nums1[2] = 3 are not present in nums2. Therefore, answer[0] = [1,3].

# For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4 and nums2[2] = 6 are not present in nums2. Therefore, answer[1] = [4,6].

def find_disjoint_elements(nums1, nums2):
    distinct_nums1 = set(nums1)
    distinct_nums2 = set(nums2)

    answer = [[], []]

    for num in distinct_nums1:
        if num not in distinct_nums2:
            answer[0].append(num)

    for num in distinct_nums2:
        if num not in distinct_nums1:
            answer[1].append(num)

    return answer
nums1 = list(map(int,input().split()))
nums2 = list(map(int,input().split()))

result = find_disjoint_elements(nums1, nums2)
print(result)  
