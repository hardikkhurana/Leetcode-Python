# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        s=0
        self.l=0
        def trav(node,s):
            s=s+1
            if node:
                trav(node.left,s)
                if node.left == None and node.right==None:
                    self.l=max(self.l,s)
                trav(node.right,s)
        trav(root,s)
        return self.l
        