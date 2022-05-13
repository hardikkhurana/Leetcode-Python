"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        q=deque()
        q.append(root)
        while q:
            nxt=deque()
            while q:
                ele=q.popleft()
                if ele.left:
                    nxt.append(ele.left)
                if ele.right:
                    nxt.append(ele.right)
                if q:
                    ele.next=q[0]
            q=nxt
        return root