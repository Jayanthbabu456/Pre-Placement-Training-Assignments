def find_two_sum(nums, target):
   
    nums_dict = {}
    
   
    for i, num in enumerate(nums):
     
        complement = target - num
        
     
        if complement in nums_dict:
          
            return [nums_dict[complement], i]
        
      
        nums_dict[num] = i
    
  
    return []


nums = list(map(int,input().split()))
target =int(input())
result = find_two_sum(nums, target)
print(result)
