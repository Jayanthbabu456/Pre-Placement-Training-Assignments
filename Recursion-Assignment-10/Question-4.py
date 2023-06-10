# Given a string calculate length of the string using recursion.

# **Examples:**
# Input : str = "abcd"
# Output :4

# Input : str = "GEEKSFORGEEKS"
# Output :13

def calculateLength(str, index):
    if index == len(str):
        return 0
    
    return 1 + calculateLength(str, index + 1)


str = input() 
length = calculateLength(str, 0)
print("Length of the string:", length)

str = input()
length = calculateLength(str, 0)
print("Length of the string:", length)
