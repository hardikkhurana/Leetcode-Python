#User function Template for python3
class Solution:
    def minOperation(self, n):
        res=0
        while n!=1:
            if n%2==0:
                n=n//2
            else:
                n-=1
            res+=1
        return res
            
        
class Solution:
    def minOperation(self, n):
        dp=[float("inf") for i in range(n+1)]
        dp[0],dp[1]=0,1
        for i in range(1,n+1):
            if i+1<len(dp):
                dp[i+1]=min(dp[i+1],dp[i]+1)
            if i*2<len(dp):
                dp[i*2]=min(dp[i*2],dp[i]+1)
        return dp[-1]


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        ob = Solution()
        print(ob.minOperation(n))
# } Driver Code Ends