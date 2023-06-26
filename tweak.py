# let's assume if we tweak the lchild with rchild of an arbitrary node in the binary tree, then the "structure" of the tree are not changed. Then how can we determine whether two binary trees' structures are identical.

class TreeNode:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
#  solution 1:
# def is_symmetric(root):
#     if root == None:
#         return True

#     return is_mirror(root.left,root.right) 


# def is_mirror(one,two):
#     if one == None and two == None:
#         return True
#     if one == None or two == None:
#         return False

#     if not one.val == two.val:
#         return False    

#     return is_mirror(one.left,two.right) and is_mirror(one.right,two.left)

# def is_same(one ,two):
#     if one == None and two == None:
#         return True
#     if one == None or two == None:
#         return False

#     if not one.val == two.val:
#         return False    

#     return is_same(one.left,two.left) and is_same(one.right,two.right)

# def is_same_final(root):
#     if root == None:
#         return True
#     return is_same(root.left,root.right)

# def is_tweak(root):
#     if root == None:
#         return True
    
#     return is_symmetric(root) or is_same_final(root)

# solution 2:

def is_identical(one,two):
    if one == None and two == None:
        return True
    if one == None or two == None:
        return False

    if not one.val == two.val:
        return False    

    return (is_identical(one.left,two.left) and is_identical(one.right,two.right)) or (is_identical(one.left,two.right) and is_identical(one.right,two.left))