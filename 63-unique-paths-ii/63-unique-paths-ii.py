class Solution:
    def uniquePathsWithObstacles(self, matrix: List[List[int]]) -> int:
        if matrix[-1][-1]==1 or matrix[0][0]==1:
            return 0
        n=len(matrix)
        m=len(matrix[0])
        dp=[[0 for i in range(m)] for j in range(n)]
        dp[0][0]=1
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    if i-1>=0:
                        dp[i][j] += dp[i-1][j]
                    if j-1 >= 0:
                        dp[i][j] += dp[i][j-1]
        return dp[-1][-1]