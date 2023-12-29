[
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) 
-> Optional[ListNode]:
        carry=0
        dummy = ListNode()
        curr=dummy
        while l1 or l2 or carry:
            tmp=0
            if l1:
                tmp+=l1.val
                l1=l1.next
            if l2:
                tmp+=l2.val
                l2=l2.next
            if carry:
                tmp+=1
                carry=0
            carry = tmp//10
            curr.next = ListNode(tmp%10)
            curr=curr.next
        return dummy.next
