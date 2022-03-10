# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry=0
        l3=ListNode(0)
        curr=l3
        while  l1 or l2 or carry:
            temp=0
            if l1:
                temp+=l1.val
                l1=l1.next
            if l2:
                temp+=l2.val
                l2=l2.next
            temp+=carry
            curr.next=ListNode(temp%10)
            carry=temp//10
            curr=curr.next
        return l3.next            
                
               
            
"""
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a=0
        b=0
        l1=reverse(l1)
        l2=reverse(l2)
        print(l1.val,l2.val)
        while l1 or l2:
            if l1:
                a=(a*10)+l1.val
                l1=l1.next
            if l2:
                b=(b*10)+l2.val
                l2=l2.next
        print(a,b)
        head=ListNode()
        curr=head
        temp=a+b
        for i in range(len(str(a+b))):
            val=temp%10
            temp=temp//10
            curr.next=ListNode(val)
            curr=curr.next
        return(head.next)

def reverse(head):
    prev=None
    curr=head
    while curr:
        next=curr.next
        curr.next=prev
        prev=curr
        curr=next
    return(prev)
"""
