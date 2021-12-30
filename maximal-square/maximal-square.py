class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp=[[0 for j in range(len(matrix[0]))] for i in range(len(matrix)) ]
        dp.pop()
        temp=[]
        for i in matrix[-1]:
            temp.append(int(i))
        dp.append(temp)
        for j in range(len(matrix)-1):
            dp[j][-1]=int(matrix[j][-1])
        
        for i in range(len(matrix)-2,-1,-1):
            for j in range(len(matrix[0])-2,-1,-1):
                if matrix[i][j]=="0":
                    continue
                r=(dp[i][j+1])
                b=(dp[i+1][j])
                d=(dp[i+1][j+1])
                dp[i][j]=1+min(r,b,d)
        res=0
        for i in range(len(dp)):
            res=max(res,max(dp[i]))
        return res**2
"""
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp=[[0 for j in range(len(matrix[0])+1)] for i in range(len(matrix)+1)]
        res=0
        for i in range(len(matrix)-1,-1,-1):
            for j in range(len(matrix[0])-1,-1,-1):
                if matrix[i][j]=="0":
                    continue
                r=(dp[i][j+1])
                b=(dp[i+1][j])
                d=(dp[i+1][j+1])
                dp[i][j]=1+min(r,b,d)
                res=max(res,dp[i][j])
        return res**2
"""
                
                