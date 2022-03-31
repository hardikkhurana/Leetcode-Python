class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def isvalid(capacity):
            temp = 0
            days = 1
            for _ in nums:
                if temp + _ > capacity:
                    days += 1
                    temp = 0
                temp += _
            return days <= m
        
        lo, hi = max(nums) , sum(nums)
        while lo < hi:
            mid = lo + (hi-lo)//2
            if isvalid(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo