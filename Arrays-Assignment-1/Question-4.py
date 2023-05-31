# Q4. You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.

# Example 1:
# Input: digits = [1,2,3]
# Output: [1,2,4]

# Explanation: The array represents the integer 123.

# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].




def plus_one(digits):
    num_str = ''.join(str(digit) for digit in digits)  
    incremented_num = int(num_str) + 1 
    incremented_str = str(incremented_num)  
    new_digits = [int(char) for char in incremented_str]  
    return new_digits
digits = list(map(int,input().split()))
result = plus_one(digits)
print(result)