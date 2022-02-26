# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans=[0]
        
        def helper(root,s):
            if root:
                s+=str(root.val)
                if root.left==None and root.right==None:
                    ans[0]+=int(s)                    
                helper(root.left,s)
                helper(root.right,s)
        
        helper(root,"")
        return ans[0]
                
        