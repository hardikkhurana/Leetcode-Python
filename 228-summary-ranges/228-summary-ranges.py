class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums)==1:
            return [str(nums[0])]
        ans=[]
        start=0
        nxt=0
        right=1
        while len(nums)+1>right:
            while len(nums)>right and nums[nxt]+1==nums[right]:
                nxt+=1
                right+=1
            if start==nxt:
                ans.append(str(nums[start]))
            else:
                ans.append(str(nums[start])+"->"+str(nums[nxt]))
            start=right
            nxt=right
            right+=1
        return ans
                
        