class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        for i,e in enumerate(nums):
            if target-e in s:
                return [i,s[target-e]]
            s[e]=i
[2,7,11,15]
