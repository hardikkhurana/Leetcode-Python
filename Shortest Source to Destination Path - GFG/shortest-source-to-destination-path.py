#User function Template for python3
from collections import deque
class Solution:
    def shortestDistance(self,N,M,A,X,Y):
        def isValid(row: int, col: int):
            return (row >= 0) and (row < N) and (col >= 0) and (col < M)
        
        rowNum = [-1, 0, 0, 1]
        colNum = [0, -1, 1, 0]
        if A[0][0]!=1 or A[X][Y]!=1:
            return -1
        visited=[[False for j in range(M)] for i in range(N)]
        visited[0][0]=True
        q=deque()
        q.append((0,0,0))
        while q:
            currx,curry,currdis=q.popleft()
            if currx==X and curry==Y:
                return currdis
            
            for i in range(4):
                row = currx + rowNum[i]
                col = curry + colNum[i]
                if (isValid(row,col) and A[row][col] == 1 and not visited[row][col]):
                    visited[row][col] = True
                    q.append((row,col,currdis+1))
        return -1
        
        
        
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math
        
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N,M=map(int,input().strip().split())
        a=[]
        for i in range(N):
            s=list(map(int,input().strip().split()))
            a.append(s)
        x,y=map(int,input().strip().split())    
        ob=Solution()
        print(ob.shortestDistance(N,M,a,x,y))
        
# } Driver Code Ends