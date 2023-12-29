[
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        c = defaultdict(int)
        res=[]
        mlvl = -1

        def helper(node,lvl):
            if node:
                helper(node.left,lvl+1)
            nonlocal mlvl
                mlvl = max(mlvl,lvl)
                c[lvl]=node.val
                helper(node.right,lvl+1)
        helper(root,0)
        for i in range(mlvl+1):
            res.append(c[i])
        return res
