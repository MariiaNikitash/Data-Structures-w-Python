# Binary Trees II

#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*
# PROBLEM 1: Is Uni-valued
# A binary tree is uni-valued if every node in the tree has the same value.
# Given the root of a binary tree, return True if the given tree is uni-valued and False otherwise.

class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right
         
def is_univalued(root):
    if not root:
        return True
    
    def helper(node, value):
        if not node:
            return True
        if node.val != value:
            return False
        return helper(node.left, value) and helper(node.right, value)
    
    return helper(root, root.val)
print(is_univalued(root=TreeNode(1, TreeNode(1))))
    