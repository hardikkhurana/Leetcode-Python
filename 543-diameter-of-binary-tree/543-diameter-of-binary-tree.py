# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.res=0
        
        def helper(node):
            if not node.left and not node.right:
                return 0
            l,r=0,0
            if node.left:
                l=helper(node.left)+1
            
            if node.right:
                r=helper(node.right)+1
                
            self.res=max(self.res,l+r)
            return max(l,r)
        
        helper(root)
        return self.res