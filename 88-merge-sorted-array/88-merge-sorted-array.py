class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        j=m
        for i in nums2:
            nums1[j]=i
            j+=1
        nums1.sort()