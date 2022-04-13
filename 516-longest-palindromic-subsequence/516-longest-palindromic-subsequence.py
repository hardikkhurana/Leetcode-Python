class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n=len(s)
        dp=[[-1]*n for i in range(n)]
        for g in range(n):
            i=0
            j=g
            while j<n:
                if g==0:
                    dp[i][j]=1
                elif g==1:
                    if s[i]==s[j]:
                        dp[i][j]=2
                    else:
                        dp[i][j]=1
                else:
                    if s[i]==s[j]:
                        dp[i][j]=2+dp[i+1][j-1]
                    else:
                        dp[i][j]=max(dp[i+1][j],dp[i][j-1])
                i+=1
                j+=1
        return dp[0][n-1]
            
        