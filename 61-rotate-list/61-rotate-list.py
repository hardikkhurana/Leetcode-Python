# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head :
            return None
        l=1
        curr=head
        while curr.next:
            l+=1
            curr=curr.next
        k=k%l
        curr.next=head
        
        temp=head
        for i in range(l-k-1):
            temp=temp.next
        ans=temp.next
        temp.next=None
        return ans
        