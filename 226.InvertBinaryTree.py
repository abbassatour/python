#AI 

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base case: empty node
        if not root:
            return None
        
        # Swap the left and right children
        root.left, root.right = root.right, root.left
        
        # Recurse on both subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root

#Time Complexity: O(N)
#Space Complexity: O(N) and in best cases : O(log N)
# Because of the Call Stack