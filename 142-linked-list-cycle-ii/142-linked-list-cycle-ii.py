# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow=fast=head
        pos=1
        if not head:
            return None
        if not head.next:
            return None
        if not head.next.next:
            return None
        while fast.next and fast.next.next:
            fast=fast.next.next
            slow=slow.next
            if slow==fast:
                break
        if slow==fast:
            while head!=fast:
                head=head.next
                fast=fast.next
            return head
        else:
            return None