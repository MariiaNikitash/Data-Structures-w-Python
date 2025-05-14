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
    
#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*
# PROBLEM 2: Binary Tree Height
def height(root):
    if not root:
          return 0
    # Return the max height of the two subtrees, plus 1 for the current node
    return 1 + max(height(root.left), height(root.right))
#Time O(n)
#Space O(h)
#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*
# PROBLEM 3: binary tree insert
#  insert new node with a given key and value into the tree.
# Return root of modified tree. The tree is sorted by key.
# If a node with given key already exists, update existing key’s value. 
class TreeNode():
     def __init__(self, key, value, left=None, right=None):
            self.key = key
            self.val = value
            self.left = left
            self.right = right

def insert(root, key, value):
    if not root:
          return TreeNode(key, value)
    if key < key.root:
         return insert(root.left, key, value)
    elif key > key.root:
         return insert(root.right, key, value)
    elif key == key.root:
         root.val = value
    return root
# Time: Log N, but if tree is skewed its N
# Spaace O(H)
     