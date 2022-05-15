# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        self.l=[0]
        
        def helper(node,k):
            if node:
                helper(node.left,k+1)
                if k>self.l[0]:
                    self.l=[k]
                    self.l.append(node.val)
                elif k==self.l[0]:
                    self.l.append(node.val)
                helper(node.right,k+1)
        
        helper(root,1)
        return sum(self.l[1:])
        