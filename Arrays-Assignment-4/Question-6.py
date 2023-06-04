# Given an integer array nums sorted in **non-decreasing** order, return *an array of **the squares of each number** sorted in non-decreasing order*.

# **Example 1:**

# Input: nums = [-4,-1,0,3,10]

# Output: [0,1,9,16,100]

# **Explanation:** After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100]

def sorted_squares(nums):
    squares = [num * num for num in nums]
    squares.sort()
    return squares

nums =list(map(int,input().split()))
result = sorted_squares(nums)
print(result)  
