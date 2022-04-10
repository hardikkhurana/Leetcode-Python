class Solution:
    def calPoints(self, ops: List[str]) -> int:
        res=[]
        for i in ops:
            if i=="+":
                res.append(res[-1]+res[-2])
            elif i=="D":
                res.append(res[-1]*2)
            elif i=="C":
                res.pop()
            else:
                res.append(int(i))
        return sum(res)