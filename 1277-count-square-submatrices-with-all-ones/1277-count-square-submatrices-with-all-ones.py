class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        n=len(matrix)
        m=len(matrix[0])
        dp=[[0 for j in range(m+1)] for i in range(n+1)]
        ans=0
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                if matrix[i][j]==1:
                    dp[i][j]=min(dp[i+1][j],dp[i][j+1],dp[i+1][j+1])+1
                    ans+=dp[i][j]
        return ans
        
        