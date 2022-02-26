class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex==0:
            return [1]
        if rowIndex==1:
            return [1,1]
        dp=[1,2,1]
        for i in range(2,rowIndex):
            temp=[1]
            for i in range(len(dp)-1):
                temp.append(dp[i]+dp[i+1])
            temp.append(1)
            dp=temp
        return dp