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
                