# Given a string, count total number of consonants in it. A consonant is an English alphabet character that is not vowel (a, e, i, o and u). Examples of constants are b, c, d, f, and g.

# **Examples :**
# Input : abc de
# Output : 3
# There are three consonants b, c and d.

# Input : geeksforgeeks portal
# Output : 12

def countConsonants(s):
    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    s = s.lower()
    for char in s:
        if char.isalpha() and char not in vowels:
            count += 1
    return count


s = input() 
print("Total consonants:", countConsonants(s))

s = input()
print("Total consonants:", countConsonants(s))
