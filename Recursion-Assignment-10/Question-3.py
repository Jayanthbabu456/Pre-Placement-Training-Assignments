# Given a set represented as a string, write a recursive code to print all subsets of it. The subsets can be printed in any order.

# **Example 1:**

# Input :  set = “abc”

# Output : { “”, “a”, “b”, “c”, “ab”, “ac”, “bc”, “abc”}

# **Example 2:**

# Input : set = “abcd”

# Output : { “”, “a” ,”ab” ,”abc” ,”abcd”, “abd” ,”ac” ,”acd”, “ad” ,”b”, “bc” ,”bcd” ,”bd” ,”c” ,”cd” ,”d” }

def generateSubsets(set, subset, index):
    if index == len(set):
        print(subset)
        return

    generateSubsets(set, subset + set[index], index + 1)
    generateSubsets(set, subset, index + 1)


set = input()
generateSubsets(set, "", 0)

set = input()
generateSubsets(set, "", 0)
