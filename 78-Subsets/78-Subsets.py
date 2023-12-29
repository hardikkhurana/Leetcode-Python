[
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        
        def helper(ind,curr):
            if ind==len(nums):
                res.append(curr.copy())
            helper(ind+1,curr)
            curr.append(nums[ind])
            helper(ind+1,curr)
            curr.pop()
        helper(0,[])
                return
        return res
