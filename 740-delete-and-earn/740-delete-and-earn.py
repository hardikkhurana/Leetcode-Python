class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        d=Counter(nums)
        nums=sorted(list(set(nums)))
        
        
        earn1,earn2=0,0
        for i in range(len(nums)):
            curr=nums[i]*d[nums[i]]
            if i>0 and nums[i]==nums[i-1]+1:
                temp=earn2
                earn2=max(earn1+curr,earn2)
                earn1=temp
            else:
                temp=earn2
                earn2=earn2+curr
                earn1=temp
        return earn2
                