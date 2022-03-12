# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
from collections import deque
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans=defaultdict(list)
        if root is None:
            return []
        q=deque()
        q.append((root,0,0))
        while len(q)>0:
            node,x,y=q.popleft()
            ans[x].append((abs(y),node.val))
            if node.left is not None:
                q.append((node.left,x-1,y-1))
            if node.right is not None:
                q.append((node.right,x+1,y-1))
            
        res=[]
        for key in sorted(ans.keys()):
            res.append(ele[1] for ele in sorted(ans[key]))
        return res