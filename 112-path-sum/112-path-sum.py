# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        a=[False]
        def helper(node,s):
            if node:
                s=s+node.val
                if node.right==None and node.left==None:
                    if s==targetSum:
                        a[0]=True
                        return 
                helper(node.left,s)
                helper(node.right,s)
        helper(root,0)
        return a[0]
        