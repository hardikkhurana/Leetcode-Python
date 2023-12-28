[
#�Definition�for�a�binary�tree�node.
#�class�TreeNode:
#�����def�__init__(self,�val=0,�left=None,�right=None):
#���������self.val�=�val
#���������self.left�=�left
#���������self.right�=�right
class�Solution:
����def�maxDepth(self,�root:�Optional[TreeNode])�->�int:

��������def�helper(node):
������������if�not�node:
����������������return�0
������������
������������l�=�helper(node.left)
������������r�=�helper(node.right)

������������return�1+max(l,r)
��������
��������return�helper(root)
