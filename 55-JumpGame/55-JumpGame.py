[2,3,1,1,4]
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i=0
        mx=0
        for i in range(len(nums)):
            if i>mx:
                return False
            mx = max(mx,nums[i]+i)
        return True
