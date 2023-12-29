[
class Solution:
    def maxArea(self, h: List[int]) -> int:
        l,r=0,len(h)-1
        res=min(h[l],h[r])*(r-l)
        while l<r:
            if h[l]<=h[r]:
                l+=1
            else:
                r-=1
            res=max(res,min(h[l],h[r])*(r-l))
        return res
