[
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n,m = len(grid),len(grid[0])
        
        dp=[[float("inf")]*(m+1) for _ in range(n+1)]

        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                dp[i][j] = grid[i][j]+min(dp[i+1][j],dp[i][j+1])
        
        for d in dp:
            print(d)
        dp[-1][m-1]=0
        return dp[0][0]
