# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        def dfs(i,j,nums):
            if i > j:
                return None
            mid = (i+j)//2
            node = TreeNode(nums[mid])
            node.left = dfs(i,mid-1,nums)
            node.right = dfs(mid+1,j,nums)
            
            return node
        return dfs(0,len(nums)-1,nums)