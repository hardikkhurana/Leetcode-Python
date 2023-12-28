5
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==1:
            return [[1]]
        if numRows==2:
            return [[1],[1,1]]
        res=[[1],[1,1]]

        for i in range(numRows-2):
            tmp =[1]
            for i in range(len(res[-1])-1):
                tmp.append(res[-1][i]+res[-1][i+1])
            tmp.append(1)
            res.append(tmp)
        return res
