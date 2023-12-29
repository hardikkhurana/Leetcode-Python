"
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp=[False for _ in range(len(s)+1)]
        wordDict = set(wordDict)
        dp[-1]=True
        for i in range(len(s)-1,-1,-1):
            for j in range(i,len(s)):
                if s[i:j+1] in wordDict:
                    dp[i] = dp[i] or dp[j+1]
        return dp[0]
