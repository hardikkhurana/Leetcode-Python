class Solution:
    def numberOfSteps(self, num: int) -> int:
        res=0
        while num:
            if num%2==0:
                num=num//2
            else:
                num-=1
            res+=1
        return res