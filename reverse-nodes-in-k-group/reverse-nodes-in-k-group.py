#0-1 -4-5-6-7-8-9-10,k=3


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getting_Kth(self,curr,k):
        while curr and k>0:
            curr=curr.next
            k-=1
        return curr
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        groupPrev=dummy
        
        while True:
            k_next=self.getting_Kth(groupPrev,k)

            #could be none
            if not k_next:
                break
            
            groupNext=k_next.next
                
            prev=k_next.next
            curr=groupPrev.next
            #reversing
            while curr!=groupNext:
                temp=curr.next
                curr.next=prev
                prev=curr
                curr=temp
            #redefining
            temp=groupPrev.next
            groupPrev.next=k_next
            groupPrev=temp
            
        return dummy.next
                
                
                
        
        
        
        