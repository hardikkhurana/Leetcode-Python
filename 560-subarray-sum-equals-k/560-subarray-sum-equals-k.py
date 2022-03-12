"""
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=[0]
        n=len(nums)
        def helper(index,total):
            if total==k:
                count[0]+=1
            if index==n-1:
                return
            helper(index+1,total+nums[index+1])
        for i in range(len(nums)):
            helper(i,nums[i])
        return(count[0])
"""
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d=defaultdict(int)
        d[0]=1
        count=0
        s=0
        n=len(nums)
        for num in nums:
            s+=num
            if s-k in d:
                count+=d[s-k]    
            d[s]+=1
        return count
        
        