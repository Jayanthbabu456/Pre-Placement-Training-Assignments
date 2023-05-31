def plus_one(digits):
    num_str = ''.join(str(digit) for digit in digits)  
    incremented_num = int(num_str) + 1 
    incremented_str = str(incremented_num)  
    new_digits = [int(char) for char in incremented_str]  
    return new_digits
digits = list(map(int,input().split()))
result = plus_one(digits)
print(result)