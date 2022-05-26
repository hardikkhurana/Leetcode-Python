class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        a=float("-inf")
        b=float("-inf")
        for i in nums:
            a=max(i,(i+a))
            b=max(a,b)
        return b