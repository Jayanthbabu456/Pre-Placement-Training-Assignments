#  Given three integer arrays arr1, arr2 and arr3 **sorted** in **strictly increasing** order, return a sorted array of **only** the integers that appeared in **all** three arrays.

# Example 1:

# Input: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]

# Output: [1,5]

# Explanation: Only 1 and 5 appeared in the three arrays.

def common_elements(arr1, arr2, arr3):
    c_elements = []
    i, j, k = 0, 0, 0  
    while i < len(arr1) and j < len(arr2) and k < len(arr3):
        if arr1[i] == arr2[j] == arr3[k]:
            c_elements.append(arr1[i])
            i += 1
            j += 1
            k += 1
        elif arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr3[k]:
            j += 1
        else:
            k += 1

    return c_elements
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
arr3 = list(map(int,input().split()))

result = common_elements(arr1, arr2, arr3)
print(result) 
