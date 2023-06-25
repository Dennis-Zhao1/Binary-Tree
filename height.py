class TreeNode:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

def get_height(root):
    if root == None:
        return 0

    return max(get_height(root.left),get_height(root.right)) + 1
# O(n)    # 

myTree = TreeNode(5,TreeNode(4,TreeNode(6,TreeNode(8,TreeNode(9))),TreeNode(6,TreeNode(8,TreeNode(9)))),TreeNode(4,TreeNode(6,TreeNode(8,TreeNode(9)))))

print(get_height(myTree)) 
