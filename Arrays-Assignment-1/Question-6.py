def contains_duplicate(nums):
    return len(nums) != len(set(nums))
nums = list(map(int,input().split()))
result = contains_duplicate(nums)
print(result)
