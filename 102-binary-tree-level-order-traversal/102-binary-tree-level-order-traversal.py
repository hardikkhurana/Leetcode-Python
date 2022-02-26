# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        l=[]
        def helper(root,k):
            if root:
                if len(l)<k+1:
                    l.append([root.val])
                else:
                    l[k].append(root.val)
                helper(root.left,k+1)
                helper(root.right,k+1)
        helper(root,0)
        return l