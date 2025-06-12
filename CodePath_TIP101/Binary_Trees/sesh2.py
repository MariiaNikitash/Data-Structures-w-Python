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


#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*
# PROBLEM 4: binary tree remove
# The tree is sorted by key. If multiple nodes with the given key exist, remove the
# first node you find. If you need to remove a node with two children, use the in-order successor of that node,
# which is the smallest value in its right subtree.
def remove_bst(root, key):
    if not root:
        return None
    if key > root.key:
        root.right = remove_bst(root.right, key)
    elif key < root.key:
        root.left = remove_bst(root.left, key)
    elif key == root.key:
        # it removes current node, and points it to None if no childs, or if ONE child, to that child
        if not root.right:
            return root.left
        elif not root.left:
            return root.right
        elif root.left and root.right: # if 2 childs exist we do a in-order successor
            pred = root.right
            while pred.left:
                pred = pred.left
            root.key = pred.key
            root.val = pred.val
    return root

# time/space: O(h)    


#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*
# Problem 5: BST In-order Successor
# in-order successor is the node with the smallest key greater than the key of the given node.
def inorder_successor(root, node):
    def find_min(node):
        while node.left:
            node = node.left
        return node

    if node.right:
        return find_min(node.right)
    
    successor = None
    while root:
        if node.val < root.val:
            successor = root
            root = root.left
        elif node.val > root.val:
            root = root.right
        else:
            break
    return successor
    
# I dont get this sh

#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*
# Problem 6: BST In-order Successor
def merge_trees(self, root1, root2):
    if not root1 and not root2:
        return None
    v1 = root1.val if root1 else 0
    v2 = root2.val if root2 else 0
    # Merge the values if both nodes are present
    root = TreeNode(v1+v2)
    root.left = merge_trees(v1.left if v1 else None , v2.left if v2 else None)
    root.right = merge_trees(v1.right if v1 else None, v2.right if v2 else None)

    return root
# TIme O(N+M)vbc we raverse 2 trees
#Space O(h) height of deepest tree


#--------------------- Problem Set Version 2 -------------------------------------
#                            (Below)


#--------------------- Problem Set Version 3 -------------------------------------
#                            (Below)
