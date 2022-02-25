class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values={}
        for i in range(len(nums)):
            find=target-nums[i]
            if find in values:
                return [i,values[find]]
            values[nums[i]]=i
            
        