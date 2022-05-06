# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.res=0
        def helper(node,h):
            if node:
                helper(node.left,h+1)
                self.res=max(h,self.res)
                helper(node.right,h+1)
        helper(root,1)
        return self.res