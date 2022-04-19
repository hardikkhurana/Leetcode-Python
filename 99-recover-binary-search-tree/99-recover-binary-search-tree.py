# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.prev=None
        self.first=None
        self.second=None
        def inorder(node):
            if node==None:
                return
            inorder(node.left)
            if self.prev!=None and node.val<self.prev.val:
                if self.first==None:
                    self.first=self.prev
                self.second=node
            self.prev=node
            inorder(node.right)
            
        if root==None:
            return 
        inorder(root)
        #print(self.first.val,self.second.val)
        self.first.val,self.second.val=self.second.val,self.first.val
        
        