class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        l=[]
        def helper(i,s):
            if i==n:
                l.append(s.copy())
                return
            s.append(nums[i])
            helper(i+1,s)
            s.pop()
            helper(i+1,s)
        helper(0,[])
        return l