# Balanced binary tree: is commonly defined as a binary tree in which the depth of the left and right subtrees of every node differ by 1 or less

# Complete binary tree: is a binary tree in which every level, except possibly the last, is completely filled, and all nodes are as far left as possible

# Binary search tree: is a binary tree for every single node in the tree, the valuse in its left subtree are all smaller than its value, and the values in its right subtree are all larger than its value

# 1. how to determine whether a binary tree is a balanced binary tree?
class TreeNode:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

def is_balanced(root):
    if root == None:
        return True
    l = get_height(root.left)
    r = get_height(root.right)

    if (abs(left - right) > 1):
        return False
    return is_balanced(root.left) and is_balanced(root.right)


def get_height(root):
    if root == None:
        return 0

    return max(get_height(root.left),get_height(root.right)) + 1