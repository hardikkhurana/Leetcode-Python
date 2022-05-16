class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        r=len(grid)
        c=len(grid[0])
        if grid[0][0] or grid[r-1][c-1]:
            return -1
        def valid(a,b):
            return a>=0 and b>=0 and a<r and b<c
        q=deque()
        q.append((0,0,1))
        direction=[[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
        while q:
            x,y,res=q.popleft()
            if x==r-1 and y==c-1:
                print("wow")
                return res
            for xi,yj in direction:
                if valid(x+xi,y+yj) and grid[x+xi][y+yj]==0:
                    grid[x+xi][y+yj]=1
                    q.append((x+xi,y+yj,res+1))
        return -1
                    
            