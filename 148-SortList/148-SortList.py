[
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst = []
    
    ····while·head:
············lst.append(head.val)
············head·=·head.next
············
········lst.sort()
········dummy·=·cur·=·ListNode(0)
········for·num·in·lst:
············tmp·=·ListNode(num)
············cur.next·=·tmp
············cur·=·cur.next
············
········return·dummy.next
