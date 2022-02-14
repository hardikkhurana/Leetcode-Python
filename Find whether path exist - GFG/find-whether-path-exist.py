
from collections import deque
class Solution:
    #Function to find whether a path exists from the source to destination.
	def is_Possible(self, grid):
	    
	    N,M = len(grid),len(grid[0])
	    for i in range(N):
	        for j in range(M):
	            if grid[i][j]==1:
	                X1,Y1=i,j
	            if grid[i][j]==2:
	                X2,Y2=i,j
	                
	    def isvalid(row,col):
	        return row>=0 and row<N and col>=0 and col<M
	   
	    rowNum=[-1,0,0,1]
	    colNum=[0,-1,1,0]
	    visited=[[False for i in range(M)] for j in range(N)]
	    visited[X1][Y1]=True
	    q=deque()
	    q.append((X1,Y1))
	    while q:
	        x,y=q.popleft()
	        if x==X2 and y==Y2:
	            break
	        for i in range(4):
	            row,col=x+rowNum[i],y+colNum[i]
	            if isvalid(row,col) and (grid[row][col]==3 or grid[row][col]==2) and visited[row][col]==False:
	                visited[row][col]=True
	                q.append((row,col))
	                
	    return visited[X2][Y2]
	            
	    

#{ 
#  Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		grid = []
		for _ in range(n):
			a = list(map(int, input().split()))
			grid.append(a)
		obj = Solution()
		ans = obj.is_Possible(grid)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends