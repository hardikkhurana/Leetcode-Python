class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        l=self.helper(nums,target,True)
        r=self.helper(nums,target,False)
        if l==-1:
            return
        return [k for k in range(l,r+1)]
    
    
    
    
    def helper(self,nums,target,LeftBias):
        l,r=0,len(nums)-1
        i=-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]<target:
                l=mid+1
            elif nums[mid]>target:
                r=mid-1
            else:
                i=mid
                if LeftBias:
                    r=mid-1
                else:
                    l=mid+1
        return i    