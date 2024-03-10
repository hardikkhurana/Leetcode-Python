# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def helper(node):
            if not node:
                return 0,0 #[withroot,withoutroot]
            
            leftPair = helper(node.left)
            rightPair = helper(node.right)

            withRoot = node.val + leftPair[1] + rightPair[1]

            withoutRoot = max(leftPair) + max(rightPair)

            return withRoot,withoutRoot
            
        return max(helper(root))
[3,2,3,null,3,null,1]
