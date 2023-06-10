# We are given a string S, we need to find count of all contiguous substrings starting and ending with same character.

# **Examples :**
# Input  : S = "abcab"
# Output : 7
# There are 15 substrings of "abcab"
# a, ab, abc, abca, abcab, b, bc, bca
# bcab, c, ca, cab, a, ab, b
# Out of the above substrings, there
# are 7 substrings : a, abca, b, bcab,
# c, a and b.

# Input  : S = "aba"
# Output : 4
# The substrings are a, b, a and aba

def countContiguousSubstrings(S):
    count = 0
    prev = ""
    for i in range(len(S)):
        count += 1
        if S[i] == prev:
            count += i
        prev = S[i]
    return count


S = input()
count = countContiguousSubstrings(S)
print("Count of contiguous substrings:", count)

S = input()
count = countContiguousSubstrings(S)
print("Count of contiguous substrings:", count)
