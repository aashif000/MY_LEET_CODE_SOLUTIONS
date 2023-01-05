# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        else:
            l = self.maxDepth(root.left)
            r = self.maxDepth(root.right)

            if(l>r):
                return 1+l
            else:
                return 1+r    
