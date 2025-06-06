# Binary Trees

# Inorder: Left → Node → Right
# inorder(node.left)
# res.append(node.val)
# inorder(node.right)
# 
# # Preorder: Node → Left → Right
# res.append(node.val)
# preorder(node.left)
# preorder(node.right)
# 
# # Postorder: Left → Right → Node
# postorder(node.left)
# postorder(node.right)
# res.append(node.val)

#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*
# PROBLEM 1: Build a Binary Tree I

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

#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*
# PROBLEM 2: 3-Node Sum I
# tree has exactly 3 nodes: root, left, right
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def check_tree(root):
    if root.val == (root.left.val + root.right.val):
        return True
    return False

#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*
# PROBLEM 3: 3-Node Sum II
# tree has at most 3 nodes: root, left, right
#  return True if the value of the root is equal to the sum of the values of its two children. Return False otherwise.

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def check_tree(root):
    if not root:
        return False
    elif root.left and root.right:
        return root.val == (root.left.val + root.right.val)
    elif root.left:
        return root.val == root.left.val
    else:
        return root.val == root.right.val
    
    
# Or
def check_tree(root):
    if not root:
        return False
    left_c = right_c = 0
    if root.left:
        left_c = root.left.val
    if root.right:
        right_c = root.right.val
    sum = left_c + right_c
    return root.val == sum

#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*
# PROBLEM 4: Find Leftmost Node I

# Given the root of a binary tree, write a function
# that finds the value of the left most node in the tree.

class TreeNode1:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def left_most(root):
    if not root:
        return None
    if not root.left:
        return root.val
    return left_most(root.left)

# Time: O(n)
# Space: O(1)

#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*
# Problem 5: Find Leftmost Node II
# implement iteratively

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def left_most(root):
    if not root:
        return None
    current = root # in case root is the left most 
    while root.left:
        current = root.left
    return current.val
        
# Time: O(n)
# Space: O(1)

#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*
# PROBLEM 6: In-order Traversal
# return a list representing the inorder traversal of its nodes' values

class TreeNode():
     def __init__(self, val, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def inorder_traversal(root):
    if not root:
        return []
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)

root = TreeNode(2, TreeNode(1), TreeNode(3))
#print(inorder_traversal(root))
# Time: O(n^2) bc of list concatination
# Space: O(n)

# OR
def inorder_traversal(root):
    res = []
    def inorder(node):
        if not node:
            return 
        inorder(node.left)
        res.append(node.val)
        inorder(node.right)
    
    inorder(root)    
    return res
        
#print(inorder_traversal(root))
# Time: O(n)
# Space: O(n)


# OR
# Iteratively
def inorder_traversal(root):
    res = []
    stack = []
    cur = root
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        res.append(cur.val)
        cur = cur.right
    return res

#print(inorder_traversal(root))


#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*
# PROBLEM 7: Binnary Tree Size
# return number of nodes in the binary tree.

class TreeNode():
     def __init__(self, val, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
   
def size(root):
    if not root:
        return 0
    return 1 + size(root.left) + size(root.right) 

# Time: O(n)  Each node is processed once
# Space: O(h)  Each recursive call adds a new stack frame to the call stack
            # The maximum depth of the call stack is the height of the tree (h)
#if the tree is balanced, the height h will be log₂(n), leading to a space complexity of O(log(n)).

# Iteratively also DFS
# most common;y so;ved with stack 
def size(root):
    if not root:
        return 0
    stack = [root]
    count = 0
    while stack:
        node = stack.pop()
        count +=1
        
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return count 

# Time: O(n) 
# Space: O(h), 'h' means depends on height, Best case(balanced tree) -> O(log n)

#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*
#PROBLEM 8: Binary Tree Find
class TreeNode():
     def __init__(self, val, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
   
def find(root, value):
    if not root:
        return False
    if root.val == value:
        return True
    return find(root.left, value) or find(root.right, value)
# Time: O(n) 
# Space: O(h), 'h' means depends on height, Best case(balanced tree) -> O(log n)

#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*
#PROBLEM 9: Binary Search Tree Find
# returns True if there is a node with the given value in the tree.
# Assume the tree is balanced.

class TreeNode():
     def __init__(self, val, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
   
def find(root, value):
    if not root:
        return False
    if root.val == value:
        return True
    
    if root.val > value:
        return find(root.left, value)
    else:
        return find(root.right, value)

root = TreeNode(2, TreeNode(1), TreeNode(3))

#print(find(root, 3))
# Time: O(log n) on avarage 
# Space: O(log n) due to the recursion depth, which is the height of the tree in the balanced case.

# Iteravly if we want to avoid recursion or tree is deep or tree is unbalanced
    
def find(root, value):
    if not root:
        return False
    
    stack = [root]
    while stack:
        node = stack.pop()
        if node.val == value:
            return True
        
        if node.val > value:
            stack.append(node.left)
        else:
            stack.append(node.right)
    return False


#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*
#PROBLEM 10: BST Descending Leaves
# returns a list of the values of all leaves in the BST in descending order
# Assume the tree is balanced.
class TreeNode():
     def __init__(self, val, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
   
def descending_leaves(root):
    leaves = []

    def dfs(node):
        if not node:
            return 
        dfs(node.right)
        dfs(node.left)
        if not node.right and not node.left:
            leaves.append(node.val)

    dfs(root)
    return leaves
    

#-------------------------------- Problem Set Version 2 -----------------------------------------------

#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*
# PROBLEM 1:
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

#root = TreeNode(10, TreeNode(2),TreeNode(5))
#print(root.val, root.left.val, root.right.val)

#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*
# PROBLEM 2: 3-Node Product I (has exactly 3 nodes)
# return T if product of left * right = root

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def check_tree(root):
    if not root:
        return False
    return root.val == root.left.val * root.right.val
#print(check_tree(root))
# Time/Space: O(1)

#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*
# PROBLEM 3: 3-Node Product I (has at most 3 nodes)
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def check_tree(root):
    if not root:
        return False
    l,r = 1,1
    if root.left:
        l = root.left.val
    if root.right:
        r = root.right.val
    return root.val == l * r
#print(check_tree(root))


#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*
# PROBLEM 4: Find Rightmost Node I
# Given root of binary tree, write func that finds value of right most node in the tree.

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def right_most(root):
    if not root:
        return 
    if not root.right:
        return root.val
    return right_most(root.right)

#print(right_most(root))

#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*
# PROBLEM 5: Find Rightmost Node II
# Iteratively
def right_most(root):
    if not root:
        return 
    current = root
    while current.right:
        current = current.right
    return current.val
#print(right_most(root))

#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*
# PROBLEM 6: Post-order Traversal
# Given the root of a binary tree, return a list representing the postorder traversal
class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right

def postorder_traversal(root):
    result = []
    def postorder(node):
        if not node:
            return
        postorder(node.left)
        postorder(node.right)
        result.append(node.val)

    postorder(root)
    return result

# Time/Space: O(n)

# Iteratively
def postorder_traversal(root):
    if not root:
        return []
    
    result = []
    stack = [root]
    while stack:
        node = stack.pop()
        result.append(node.val)

        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)


    return stack[::-1] # REverse to get postorder
# Time/Space: O(n) although reversing a stack takes up O(n) space/time itself

#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*
# PROBLEM 7: Binary Tree Product
# write a function that returns the product of all nodes’ values in a binary tree.
class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right
   
def product_tree(root):
    if not root:
        return 1
    return root.val * product_tree(root.left) * product_tree(root.right)

# so for 
#      4
#     / \
#    /   \
#   2     5
#  / \    
# 1   3    

# we have product_tree(1) → 1
# product_tree(3) → 3
# product_tree(2) → 2 * 1 * 3 = 6
# product_tree(5) → 5
# product_tree(4) → 4 * 6 * 5 = 120
# Time  O(n)
# #Space: O(h)
root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(5))
#print(product_tree(root))

#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*
# PROBLEM  8: Binary Tree Is Leaf
# return True if a node with the given value is a leaf node and False otherwise
class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right
   
def is_leaf(root, value):
    if not root:
        return False

    if root.value == value:
        return root.left is None and root.right is None
    return is_leaf(root.left, value) or is_leaf(root.right, value)
# Time Complexity: O(n) where n is the number of nodes in the tree, as the worst case requires visiting every node.
# Space Complexity: O(h) where h is the height of the tree, due to recursion. This could be O(n) in a skewed tree.


#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*
# PROBLEM 9: BST Is Leaf
# returns True if a node with the given value is a leaf node and False otherwise. tree is balanced
class TreeNode():
     def __init__(self, val, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
   
def is_leaf_bst(root, value):
    if not root:
        return False
    if root.val == value:
        return True
    elif root.val > value:
        return is_leaf(root.left, value)
    else:
        return is_leaf(root.right, value)

   #Time Space O(lon n)
   
#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*
# PROBLEM 10: BST Is Full
# returns True if the tree is full and False otherwise.
# A binary tree is full if every node has either zero or two children.
   
def is_full_tree(root):
    if not root:
        return True
    if root.left is None and root.right is None:
        return True
    if root.left and root.right: 
        return is_full_tree(root.left) and is_full_tree(root.right)
    # if only 1 child is not a full tree
    return False
#print(is_full_tree(root))

#Time/space: O(n), O(h)


#-------------------------------- Problem Set Version 3 -----------------------------------------------

#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*
# PROBLEM 2: 3-Node Booleans
# Evaluates a boolean operation ('AND' or 'OR') stored in the root node on its two child nodes.
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_expression(root):
    
    left_child = root.left.val
    right_child = root.right.val

    if root.val == 'AND':
        return left_child and right_child
    elif root.val == 'OR':
        return left_child or right_child
    return False
#space/time: O(1)


#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*
# PROBLEM 3: 3-Node Equality
# binary tree that has at most 3 nodes: the root, its left child, and its right child.
# Return True if the root’s children have equal value and False otherwise.

def equality(root):
    if not root:
        return False
    if root.left and root.right:
        return root.left.val == root.right.val
    return False


#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*
# PROBLEM 4: Find Leftmost Path I
# returns a list of the left most path of the tree

def left_path(root):
    if not root:
        return []
    return [root.val] + left_path(root.left)


#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*
# PROBLEM 5: Find Leftmost Path II
# returns a list of the left most path of the tree ITERavely

def left_path(root):
    if not root:
        return []
    res = []
    node = root
    while node:
        res.append(node.val)
        node = node.left
    return res 
# Time O(h) bc we go left as long as we get to leaf
# Space O(h) bc we use list, size of which depends on how deep left node is

#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*
# PROBLEM 6: Pre-order Traversal
# current node, then the left subtree, then the right subtree.
#     1
#     / \
#    /   \
#   2     5
#  / \    
# 4   3 
#"""
# Input: root = 1
# Expected Output: [1,2,4,3,5]

def preorder_traversal(root):
    res = []
    def preorder(node):
        if not node:
            return 
        res.append(node.val)
        preorder(node.left)
        preorder(node.right)
    preorder(root)
    return res

# Time/Space: O(n)

 # Iteravely  
def preorder_traversal(root):
    res = []
    stack = [root]
    while stack:
        node = stack.pop()
        res.append(node.val)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return res

#Time/Space = O(n)

#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*
# PROBLEM 7: Binary Tree All Lesser
# return True if all nodes in tree have value less than val and False otherwise. If tree is empty, return False.

def is_lesser(root, value):
    if not root:
        return False
    if root.val >= value:
        return False
    return is_lesser(root.left, value) and is_lesser(root.right, value)

#Time/Space = O(n)


#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*
# PROBLEM 8: Binary Tree Any Greater
# returns True if any nodes greater than value exist in the tree.
# If no node greater than value exist, return False. Assume the tree is balanced.

def contains_greater(root, value):
    if not root:
        return False
    if root.val > value:
        return True
    return contains_greater(root.left, value) or contains_greater(root.right, value) 

#Time/Space = O(n)
#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*
# PROBLEM 9: Binary Search Tree Any Greater

   
def contains_greater_bst(root, value):
    if not root:
        return False
    if root.val > value:
        return True
    return contains_greater_bst(root.right, value) # root.val <= value, then only the right subtree could possibly contain a greater value (due to BST rules
# time log n
# space log n


#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*
# PROBLEM 10: BST Leaves Sum to Root
# returns True if the sum of the values of all the leaves equal the sum of the value of the root. Return False otherwise.
   
def sum_leaves(root):
    "compares root value to leaf sum"
    if not root:
        return False

    def leaf_sum(node):  
        "helpeer does recursion till it reaches leaves that it returns the value and sums them"
        if not root:
            return 0
        if root.left is None and root.right is None:
            return node.val
        return leaf_sum(node.left) + leaf_sum(node.right)
    
    return root.val == leaf_sum(root)

# time O N since i need to go all the way till the leaves
# space is O H bc of recursion stack

