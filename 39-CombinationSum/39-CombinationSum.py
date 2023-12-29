[
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List
[List[int]]:

        res= []

        def helper(ind,s,curr):
            if s==target:
                res.append(curr.copy())
                return 
            if s>target or ind==len(candidates):
                return
            
            helper(ind+1,s,curr)
            curr.append(candidates[ind])
            helper(ind,s+candidates[ind],curr)
            curr.pop()

        helper(0,0,[])
        return res
