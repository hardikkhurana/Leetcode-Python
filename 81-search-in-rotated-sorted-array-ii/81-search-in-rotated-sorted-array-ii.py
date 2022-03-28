class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        return True if target in nums else False
"""
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left=0
        right=len(nums)-1
        while low<right:
            mid=(left+right)//2
            if mid==target:"""