# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def helper(node,s):
            if not node:
                return False
            s+=node.val
            if node.right==None and node.left==None and s==targetSum:
                return True
            return helper(node.left,s) or helper(node.right,s)
        return helper(root,0)
