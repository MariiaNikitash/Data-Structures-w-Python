# Binary Trees

# Inorder: Left → Node → Right
# inorder(node.left)
# res.append(node.val)
# inorder(node.right)
# 
# # Preorder: Node → Left → Right
# res.append(node.val)
# inorder(node.left)
# inorder(node.right)
# 
# # Postorder: Left → Right → Node
# inorder(node.left)
# inorder(node.right)
# res.append(node.val)

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

# Problem 2: 3-Node Sum I
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

# Problem 3: 3-Node Sum II
# tree has at most 3 nodes: root, left, right
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


# Problem 4: Find Leftmost Node I

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


# Problem 6: In-order Traversal
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
print(inorder_traversal(root))

# OR
def inorder_traversal(root):
    res = []
    def inorder(root):
        if not root:
            return []
        inorder(root.left)
        res.append(root.val)
        inorder(root.right)
    
    inorder(root)    
    return res
        
print(inorder_traversal(root))


