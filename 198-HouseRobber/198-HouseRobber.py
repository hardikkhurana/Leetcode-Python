[
class Solution:
    def rob(self, nums: List[int]) -> int:
        a,b,=0,0
        for n in nums:
            tmp = max(n+a,b)
            a=b
            b=tmp
        return b
