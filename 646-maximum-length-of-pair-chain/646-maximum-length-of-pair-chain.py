class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        n=len(pairs)
        pairs.sort()
        dp=[1 for i in range(n)]
        for i in range(1,n):
            for j in range(i):
                if pairs[j][1]<pairs[i][0]:
                    dp[i]=max(dp[i],dp[j]+1)
        return max(dp)
        