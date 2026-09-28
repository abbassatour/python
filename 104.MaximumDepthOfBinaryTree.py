#AI
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        # 1. إذا وصلنا لنهاية المسار أو كانت الشجرة فارغة، العمق هو 0
        if not root:
            return 0
        
        # 2. نسأل الفرع الأيسر عن أقصى عمق لديه
        left_depth = self.maxDepth(root.left)
        
        # 3. نسأل الفرع الأيمن عن أقصى عمق لديه
        right_depth = self.maxDepth(root.right)
        
        # 4. نختار الأكبر بينهما ونضيف 1 (الذي يمثل العقدة الحالية)
        return max(left_depth, right_depth) + 1