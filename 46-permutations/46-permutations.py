class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        l=[]
        def helper(a,n):
            if n==1:
                l.append(a.copy())
                return
            for i in range(n):
                helper(a,n-1)
                if n%2!=0:
                    a[0],a[n-1]=a[n-1],a[0]
                else:
                    a[i],a[n-1]=a[n-1],a[i]
                    
        helper(nums,len(nums))
        return l
                


"""
import itertools
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return itertools.permutations(nums)
"""