3
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:



class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return math.comb(m+n-2, m-1)

"""
        dp=[[0]*(m+1) for _ in range(n+1)]

        dp[-1][m-1]=1
        return dp[0][0]
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                dp[i][j]=dp[i+1][j]+dp[i][j+1]
"""
