class TreeNode:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

# 1. tree traverse
# (1) pre_order:
def pre_order(root):
    if root == None:
        return None
    
    print(root.val)
    pre_order(root.left)
    pre_order(root.right)
myTree = TreeNode(5,TreeNode(4,TreeNode(6,TreeNode(8,TreeNode(9)))),TreeNode(4,TreeNode(6,TreeNode(8,TreeNode(9)))))

pre_order(myTree)