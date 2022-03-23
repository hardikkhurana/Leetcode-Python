class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        res=0
        temp=target
        while temp>startValue:
            if temp%2==0:
                temp=temp//2
                res+=1
            else:
                temp=temp//2
                temp+=1
                res+=2
        if temp<startValue:
            res+=startValue-temp
        return res