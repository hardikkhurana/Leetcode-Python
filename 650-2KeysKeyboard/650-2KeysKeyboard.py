class Solution:
    def minSteps(self, n: int) -> int:
        dp=[float("inf")]*(n+1)
        dp[0]=0
        dp[1] =0

        for i in range(2,n+1):
            dp[i] = i
            for j in range(2,i):
                if i%j==0:
                    val = dp[j] + (i//j)
3
