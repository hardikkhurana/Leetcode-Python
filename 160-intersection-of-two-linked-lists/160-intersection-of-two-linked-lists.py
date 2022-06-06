# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        currA=headA
        currB=headB
        while currA!=currB:
            if currA:
                currA=currA.next
            else:
                currA=headB
            if currB:
                currB=currB.next
            else:
                currB=headA
        return currA

"""
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        visited=[]
        while headA:
            visited.append(headA)
            headA=headA.next
        while headB:
            if headB in visited:
                return headB
            headB=headB.next
""""""  
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        d=set()
        while headA or headB:
            if headA:
                if headA in d:
                    return headA
                d.add(headA)
                headA=headA.next
            if headB:
                if headB in d:
                    return headB
                d.add(headB)
                headB=headB.next 
        return None
"""