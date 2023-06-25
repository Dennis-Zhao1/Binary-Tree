# How to judge whether a binary tree is symmetric
class TreeNode:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

def is_symmetric(root):
    if root == None:
        return True

    return is_mirror(root.left,root.right) 


def is_mirror(one,two):
    if one == None and two == None:
        return True
    if one == None or two == None:
        return False

    if not one.val == two.val:
        return False    

    return is_mirror(one.left,two.right) and is_mirror(one.right,two.left)




myTree = TreeNode(5,TreeNode(4,TreeNode(6,TreeNode(8,TreeNode(9))),TreeNode(6,TreeNode(8,TreeNode(9)))),TreeNode(4,TreeNode(6,TreeNode(8,TreeNode(9)))))
print(is_symmetric(myTree))