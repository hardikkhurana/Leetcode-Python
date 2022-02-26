"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        has={None:None}
        curr=head
        while curr:
            copy=Node(curr.val)
            has[curr]=copy
            curr=curr.next
            
        curr=head
        while curr:
            copy=has[curr]
            copy.next=has[curr.next]
            copy.random=has[curr.random]
            curr=curr.next
            
            
        return has[head]