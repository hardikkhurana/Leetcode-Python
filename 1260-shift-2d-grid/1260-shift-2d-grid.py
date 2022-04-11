class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m=len(grid)
        n=len(grid[0])
        
        def posToVal(r,c):
            return r*n+c
        def valToPos(val):
            return (val//n,val%n)
        
        res=[[0]*n for i in range(m)]
        
        for i in range(m):
            for j in range(n):
                newVal=(posToVal(i,j)+k)%(n*m)
                newR,newC=valToPos(newVal)
                res[newR][newC]=grid[i][j]
        return res
                
                    
        