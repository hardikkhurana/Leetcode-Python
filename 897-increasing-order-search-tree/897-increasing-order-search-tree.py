# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        def inorder(root,res):
            if root is None:
                return None
            inorder(root.left,res)
            res.append(root.val)
            inorder(root.right,res)
            return res
        arr=inorder(root,[])
        root= curr= TreeNode(arr[0])
        for i in range(1,len(arr)):
            curr.right=TreeNode(arr[i])
            curr=curr.right
        return root