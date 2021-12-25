class Solution:
    def trap(self, height: List[int]) -> int:
        ml=[0 for i in range(len(height))]
        m=0
        for i in range(len(height)):
            ml[i]=m
            m=max(m,height[i])
        mr=[0 for i in range(len(height))]
        m=0
        for i in range(len(height)-1,-1,-1):
            mr[i]=m
            m=max(m,height[i])
        res=0
        for i in range(len(height)):
            temp=min(mr[i],ml[i])-height[i]
            if temp>0:
                res+=temp
        return res
        