[
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mx,mn=1,1

        for n in nums:
            mx,mn = max(mx*n,mn*n,n),min(mx*n,mn*n,n)
            res = max(res,mx)
            if n==0:
                mx,mn=1,1
        res=max(nums)
        return res
