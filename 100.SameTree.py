#mine
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        if not p and not q: 
            return True
        elif not p or not q: 
            return False

        if p.val != q.val : 
            return False
        
        is_left = self.isSameTree(p.left, q.left)
        
        is_right = self.isSameTree(p.right, q.right)

        if  is_left and is_right:
            return True
        else: 
            return False 

'''
[1,2,3]:
1: -> 2 : 
'''