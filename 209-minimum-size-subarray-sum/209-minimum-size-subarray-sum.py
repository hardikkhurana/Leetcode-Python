class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i=0
        j=0
        s=0
        res=float("inf")
        while j<len(nums):
            s+=nums[j]
            while s>=target:
                res=min(res,j-i+1)
                print(j,i)
                s-=nums[i]
                i+=1
            j+=1
        if res==float("inf"):
            return 0
        return res
                
            
        