"
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n,m=len(word1),len(word2)
        dp=[[0]*(m+1) for _ in range(n+1)]
        mm=m
        for i in range(m):

            dp[-1][i]=mm
            mm-=1
        nn=n
        for i in range(n):
            dp[i][-1]=nn
            nn-=1
        for d in dp:
            print(d)
        
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                if word1[i]==word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = min(dp[i+1][j],dp[i][j+1],dp[i+1][j+1])+1
        return dp[0][0]
