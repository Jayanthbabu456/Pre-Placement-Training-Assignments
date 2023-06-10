# Given an array, find a product of all array elements.

# **Example 1:**

# Input  : arr[] = {1, 2, 3, 4, 5}
# Output : 120
# **Example 2:**

# Input  : arr[] = {1, 6, 3}
# Output : 18

def findProduct(arr):
    product = 1
    for num in arr:
        product *= num
    return product


arr = list(map(int,input().split()))
result = findProduct(arr)
print(result)  

arr = list(map(int,input().split()))
result = findProduct(arr)
print(result)  
