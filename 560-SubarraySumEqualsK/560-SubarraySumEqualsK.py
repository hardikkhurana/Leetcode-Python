[
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d={0:1}
        s=0
        res=0
        for n in nums:
            s+=n
            if s-k in d:
                res+=d[s-k]
            d[s]=d.get(s,0)+1
        print(d)
        return res
