def remove_element(nums, val):
    k = 0  
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]  
            k += 1

    return k
nums = list(map(int,input().split()))
val = int(input())
result = remove_element(nums, val)
print(result,nums[:result])

