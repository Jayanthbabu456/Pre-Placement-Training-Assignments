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
