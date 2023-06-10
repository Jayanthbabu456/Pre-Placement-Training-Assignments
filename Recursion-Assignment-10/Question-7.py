# Given a string **str**, the task is to print all the permutations of **str**. A **permutation** is an arrangement of all or part of a set of objects, with regard to the order of the arrangement. For instance, the words ‘bat’ and ‘tab’ represents two distinct permutation (or arrangements) of a similar three letter word.

# **Examples:**

# Input: str = “cd”

# **Output:** cd dc

# **Input:** str = “abb”

# **Output:** abb abb bab bba bab bba

def permute(str):
    n = len(str)
    visited = [False] * n
    temp = ""
    permuteUtil(str, temp, visited, n)

def permuteUtil(str, temp, visited, n):
    if len(temp) == n:
        print(temp, end=" ")

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            temp += str[i]

            permuteUtil(str, temp, visited, n)

            visited[i] = False
            temp = temp[:-1]

str = input()
print("Permutations:")
permute(str)

str = input()
print("\nPermutations:")
permute(str)
