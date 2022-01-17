#User function Template for python3

class Solution:
    
    #Function to find length of longest increasing subsequence.
    def longestSubsequence(self,a,n):
        dp=[1 for i in range(n)]
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if a[i]<a[j]:
                    dp[i]=max(dp[i],dp[j]+1)
                    
        return max(dp)
       


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        a = [ int(x) for x in input().split() ]
        ob=Solution()
        print(ob.longestSubsequence(a,n))
# } Driver Code Ends