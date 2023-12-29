[
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float("-inf")
        mx = float("-inf")

        for n in nums:
            mx = max(mx+n,n)
            res = max(res,mx)
        return res
