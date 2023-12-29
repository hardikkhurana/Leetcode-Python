[
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n,m=len(grid),len(grid[0])

        def inside(x,y):
            return 0<=x<n and 0<=y<m
        
        def helper(i,j):
        
        for i in range(n):
            for j in range(m):
        res=0
                if grid[i][j]=="1":
                    helper(i,j)
                    res+=1
            grid[i][j]="-1"
            for I,J in [[-1,0],[0,1],[0,-1],[1,0]]:
                if inside(x,y) and grid[x][y]=="1":
                    helper(x,y)
                x,y=i+I,j+J
        return res
