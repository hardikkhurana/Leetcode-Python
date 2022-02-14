"""
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        res=[float("inf")]
        def solve(r,c,s):
            if r==len(grid) or c==len(grid[0]):
                return
            s=s+grid[r][c]
            if r==len(grid)-1 and c==len(grid[0])-1:
                res[0]=min(res[0],s)
                return
            
            solve(r+1,c,s)
            solve(r,c+1,s)
        solve(0,0,0)
        return res[0]
        """
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp=[[float("inf")]*(len(grid[0])+1) for i in range(len(grid)+1)]
        dp[-1][len(grid[0])-1]=0
        for i in range(len(grid)-1,-1,-1):
            for j in range(len(grid[0])-1,-1,-1):
                dp[i][j]=grid[i][j]+min(dp[i+1][j],dp[i][j+1])
        return dp[0][0]
    