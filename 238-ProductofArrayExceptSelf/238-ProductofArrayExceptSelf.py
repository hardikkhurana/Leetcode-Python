[
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        z=0
        p=1
        for n in nums:
            if n==0:
                z+=1
            else:
                p*=n
        if z>1:
            return [0 for _ in range(len(nums))]
        if z==1:
            return [0 if n!=0 else p for n in nums]

        return [p//n for n in nums]
