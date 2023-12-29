[
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[float("inf")]*(amount+1)
        for a in range(amount+1):
            for c in coins:
                if a-c>-1:
                    dp[a]=min(dp[a],dp[a-c]+1)
        dp[0]=0
        return dp[-1] if dp[-1]!=float("inf") else -1
