# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        
        def helper(root,l,r):
            if not root:
                return True
            return l<root.val<r and helper(root.left,l,root.val) and helper(root.right,root.val,r)
        
        return helper(root,float("-inf"),float("inf"))
    