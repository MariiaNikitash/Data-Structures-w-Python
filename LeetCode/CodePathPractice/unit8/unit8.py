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


