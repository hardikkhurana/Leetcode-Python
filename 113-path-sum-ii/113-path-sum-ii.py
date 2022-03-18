# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res=[]
        def helper(node,s,path):
            if not node:
                return
            s+=node.val
            path.append(node.val)
            if node.right==None and node.left==None and s==targetSum:
                res.append(path.copy())
            helper(node.left,s,path)
            helper(node.right,s,path)
            path.pop()
        helper(root,0,[])
        return res