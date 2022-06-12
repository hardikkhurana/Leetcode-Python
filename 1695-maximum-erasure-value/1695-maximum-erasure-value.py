class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        ans=0
        seen=set()
        l,r=0,0
        temp=0
        while r<len(nums):
            if nums[r] not in seen:
                temp+=nums[r]
                seen.add(nums[r])
                r+=1
            else:
                temp-=nums[l]
                seen.remove(nums[l])
                l+=1
            ans=max(ans,temp)
        
        return ans
        