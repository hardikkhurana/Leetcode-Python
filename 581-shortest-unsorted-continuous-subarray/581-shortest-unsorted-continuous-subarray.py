class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        lis=sorted(nums)
        l=-1
        r=-2
        
        for i in range(n):
            if lis[i]!=nums[i]:
                if l==-1:
                    l=i
                r=i
        if l==-1:
            return 0
        
        return r-l+1