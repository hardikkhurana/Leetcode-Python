# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        self.ans=target
        def helper(node):
            if node:
                helper(node.left)
                if node.val==target.val:
                    self.ans=node
                    return
                helper(node.right)  
        helper(cloned)
        return self.ans
            
        