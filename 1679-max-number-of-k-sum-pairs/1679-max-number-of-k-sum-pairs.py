class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        l=0
        r=len(nums)-1
        res=0
        while l<r:
            tot=nums[l]+nums[r]
            if tot==k:
                res+=1
                l+=1
                r-=1
            elif tot<k:
                l+=1
            else:
                r-=1
        return res
"""
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        d=Counter(nums)
        res=0
        for i in range(len(nums)):
            tmp=nums[i]
            if d[tmp]==0:
                continue
            if d[k-tmp]>0 and k-tmp!=tmp:
                res+=1
                d[tmp]-=1
                d[k-tmp]-=1
            if d[k-tmp]>1 and k-tmp==tmp:
                res+=1
                d[tmp]-=2
        return res
"""                