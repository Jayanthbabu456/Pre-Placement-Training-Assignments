# Given an array of characters chars, compress it using the following algorithm:

# Begin with an empty string s. For each group of **consecutive repeating characters** in chars:

# - If the group's length is 1, append the character to s.
# - Otherwise, append the character followed by the group's length.

# The compressed string s **should not be returned separately**, but instead, be stored **in the input character array chars**. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

# After you are done **modifying the input array,** return *the new length of the array*.

# You must write an algorithm that uses only constant extra space.

# **Example 1:**

# **Input:** chars = ["a","a","b","b","c","c","c"]

# **Output:** Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]

# **Explanation:**

# The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".

def compress(chars):
    readPtr = writePtr = 0

    while readPtr < len(chars):
        currChar = chars[readPtr]
        count = 1

        while readPtr + 1 < len(chars) and chars[readPtr + 1] == currChar:
            readPtr += 1
            count += 1

        chars[writePtr] = currChar
        writePtr += 1

        if count > 1:
            countStr = str(count)
            for digit in countStr:
                chars[writePtr] = digit
                writePtr += 1

        readPtr += 1

    return writePtr

chars = ["a","a","b","b","c","c","c"]
result = compress(chars)
print(result) 
print(chars[:result]) 
