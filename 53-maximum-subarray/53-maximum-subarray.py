class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_res=float("-inf")
        max_temp=float("-inf")
        for i in nums:
            max_temp=max(i,(i+max_temp))
            max_res=max(max_temp,max_res)
        return max_res
        
        