# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nums=[]
        def trav(head):
            if head:
                trav(head.left)
                nums.append(head.val)
                trav(head.right)
        trav(root)
        return nums[k-1]
        