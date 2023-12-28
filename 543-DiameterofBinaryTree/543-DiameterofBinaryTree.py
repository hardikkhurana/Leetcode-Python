[
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def helper(node):
            if not node:
                return 0
            
            mx = max(mx,l+r)
        
        helper(root)
        mx = 0
            nonlocal mx

            
            l,r = helper(node.left),helper(node.right)

            return max(l,r)+1
        return mx
