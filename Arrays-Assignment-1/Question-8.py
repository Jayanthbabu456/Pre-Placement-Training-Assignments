def find_error_nums(nums):
    n = len(nums)
    nums_set = set(nums)
    duplicate = sum(nums) - sum(nums_set)
    missing = (n * (n + 1) // 2) - sum(nums_set)
    return [duplicate, missing]
nums = list(map(int,input().split()))
result = find_error_nums(nums)
print(result)
