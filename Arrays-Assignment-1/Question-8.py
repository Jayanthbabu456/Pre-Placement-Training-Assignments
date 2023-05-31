# Q8.You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

# You are given an integer array nums representing the data status of this set after the error.

# Find the number that occurs twice and the number that is missing and return them in the form of an array.

# Example 1:
# Input: nums = [1,2,2,4]
# Output: [2,3]



def find_error_nums(nums):
    n = len(nums)
    nums_set = set(nums)
    duplicate = sum(nums) - sum(nums_set)
    missing = (n * (n + 1) // 2) - sum(nums_set)
    return [duplicate, missing]
nums = list(map(int,input().split()))
result = find_error_nums(nums)
print(result)
