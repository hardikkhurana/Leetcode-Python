class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n=len(s)
        dp=[False for i in range(n+1)]
        dp[-1]=True
        for i in range(n-1,-1,-1):
            for j in wordDict:
                if i+len(j)<=n:
                    if s[i:i+len(j)]==j and dp[i]==False:
                        dp[i]=dp[i+len(j)]
        return dp[0]
            
        