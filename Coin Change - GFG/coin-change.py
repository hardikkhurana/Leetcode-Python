#User function Template for python3

class Solution:
    def count(self, S, m, n): 
        dp=[[0] * (n+1) ]*(m+1)
        for i in range(m+1):
            dp[i][0]=1
            
        for i in range(1,m+1):
            for j in range(1,n+1):
                dp[i][j]=dp[i-1][j]
                if j-S[i-1]>=0:
                    dp[i][j] += dp[i][j-S[i-1]]
        return dp[-1][-1]
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n,m = list(map(int, input().strip().split()))
        S = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.count(S,m,n))
# } Driver Code Ends