class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        nums = [[j,i] for i,j in c.items()]
        nums.sort(reverse = True)
        return [j for i,j in nums][:k]
[1,1,1,2,2,3]
