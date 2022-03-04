class ListNode:
    def __init__(self,val,nxt,prev):
        self.prev=prev
        self.val=val
        self.nxt=nxt
        

class MyCircularQueue:

    def __init__(self, k: int):
        self.left=ListNode(0,None,None)
        self.right=ListNode(0,None,self.left)
        self.left.nxt=self.right
        self.k=k
        
    def enQueue(self, value: int) -> bool:
        if self.k==0:
            return False
        curr=ListNode(value,self.right,self.right.prev)
        self.right.prev.nxt=curr
        self.right.prev=curr
        self.k-=1
        return True
        
        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.left.nxt=self.left.nxt.nxt
        self.left.nxt.prev=self.left
        self.k+=1
        return True
        

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.left.nxt.val

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.right.prev.val
        

    def isEmpty(self) -> bool:
        if self.left.nxt==self.right:
            return True
        return False

    def isFull(self) -> bool:
        if self.k==0:
            return True
        return False

        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()