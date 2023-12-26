class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:

        memo={}

        def helper(i,s):
            if (i,s) in memo:
                return memo[(i,s)]
            if i==n:
                if target==s:
                    return 1
                return 0
            memo[(i,s)] = 0
            for j in range(1,k+1):
                memo[(i,s)]+=helper(i+1,s+j)
            return memo[(i,s)]
        
        return helper(0,0) % (10**9+7)
