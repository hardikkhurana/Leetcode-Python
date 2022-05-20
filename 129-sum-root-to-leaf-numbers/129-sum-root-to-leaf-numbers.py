# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.res=0
        
        def helper(node,s):
            if node:
                s+=str(node.val)
                if node.left==None and node.right==None:
                    self.res+=int(s)
                helper(node.left,s)
                helper(node.right,s)
        helper(root,"")
        return self.res