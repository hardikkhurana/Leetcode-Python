# User function Template for Python3

class Solution:
    def equalPartition(self, N, nums):
        s=sum(nums)
        if s%2!=0:
            return False
        target=s//2
        dp=set([0])
        for i in range(len(nums)-1,-1,-1):
            tempdp=set()
            for j in dp:
                tmp=j+nums[i]
                if tmp==target:
                    return True
                tempdp.add(tmp)
                tempdp.add(j)
            dp=tempdp

#{ 
#  Driver Code Starts
# Initial Template for Python3

import sys
input = sys.stdin.readline
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for it in range(N):
            arr[it] = int(arr[it])
        
        ob = Solution()
        if (ob.equalPartition(N, arr) == 1):
            print("YES")
        else:
            print("NO")
# } Driver Code Ends