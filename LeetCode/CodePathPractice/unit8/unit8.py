# Binary Trees

# Problem 1: Build a Binary Tree I

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

left_node = TreeNode(4)
right_node = TreeNode(6)
rootT = TreeNode(10, left_node, right_node)

# OR
root = TreeNode(10)
root.left = TreeNode(4)
root.right = TreeNode(6)