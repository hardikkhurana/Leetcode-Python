class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        z = 0
        p = 1
        for i,n in enumerate(nums):
            if n==0:
                z+=1
            else:
                p*=n
        if z>1:
            return [0]*len(nums)
        if z==1:
            return [0 if n!=0 else p for n in nums ]
        return [p//n for n in nums]
[1,2,3,4]
