#AI
# Iterative Approach using Stack 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # 1. Helper function: Check if two trees are identical iteratively using an explicit stack
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        # Store node pairs (one from each tree) in the stack
        stack = [(p, q)]
        
        while stack:
            node1, node2 = stack.pop()
            
            # If both nodes are null, this branch matches so far; continue to the next pair
            if not node1 and not node2:
                continue
            
            # If one is null or values differ, trees are not identical
            if not node1 or not node2 or node1.val != node2.val:
                return False
            
            # Push corresponding left and right children as pairs for future checks
            stack.append((node1.left, node2.left))
            stack.append((node1.right, node2.right))
            
        return True

    # 2. Main function: Traverse the main tree iteratively using a stack
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        # An empty main tree cannot contain any subtree
        if not root:
            return False
        
        # Stack used to traverse every node in the main tree (DFS)
        stack = [root]
        
        while stack:
            curr = stack.pop()
            
            # Check if the tree rooted at 'curr' matches 'subRoot'
            if self.isSameTree(curr, subRoot):
                return True
            
            # If not a match, push children to the stack to continue searching
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
                
        return False



#AI 
# Recursive Approach 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # 1. Helper function: Recursively check if two trees are completely identical
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        # Both trees reached null at the same time -> identical
        if not p and not q:
            return True
        # One tree is null while the other is not -> structural mismatch
        if not p or not q:
            return False
        # Values do not match
        if p.val != q.val:
            return False
        
        # Recursively check both left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    # 2. Main function: Check if 'subRoot' exists anywhere inside 'root'
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        # Base case: an empty main tree cannot contain a subtree
        if not root:
            return False
        
        # Step 1: Check if the current tree matches subRoot completely
        if self.isSameTree(root, subRoot):
            return True
        
        # Step 2: If not, search in the left OR right subtree
        # Note: pass 'subRoot' intact as the template to match against
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)