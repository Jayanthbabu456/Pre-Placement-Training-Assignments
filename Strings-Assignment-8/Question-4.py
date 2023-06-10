# You need to construct a binary tree from a string consisting of parenthesis and integers.

# The whole input represents a binary tree. It contains an integer followed by zero, one or two pairs of parenthesis. The integer represents the root's value and a pair of parenthesis contains a child binary tree with the same structure.
# You always start to construct the **left** child node of the parent first if it exists.

# **Input:** s = "4(2(3)(1))(6(5))"

# **Output:** [4,2,6,3,1,5]

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def constructTree(s):
    if not s:
        return None

   
    i = 0
    while i < len(s) and s[i].isdigit():
        i += 1
    root_val = int(s[:i])

   
    left_start = s.find('(', i)
    left_end = findClosingParenthesis(s, left_start)
    right_start = s.find('(', left_end + 1)
    right_end = findClosingParenthesis(s, right_start)

   
    left_subtree = constructTree(s[left_start + 1:left_end])
    right_subtree = constructTree(s[right_start + 1:right_end])

   
    root = TreeNode(root_val, left_subtree, right_subtree)
    return root

def findClosingParenthesis(s, start):
    count = 0
    for i in range(start, len(s)):
        if s[i] == '(':
            count += 1
        elif s[i] == ')':
            count -= 1
            if count == 0:
                return i
    return -1

s = "4(2(3)(1))(6(5))"
root = constructTree(s)

def preorderTraversal(root):
    if root is None:
        return []
    return [root.val] + preorderTraversal(root.left) + preorderTraversal(root.right)

result = preorderTraversal(root)
print(result)  
