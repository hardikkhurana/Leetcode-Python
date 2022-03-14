class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n=len(heights)
        m=len(heights[0])
        pac=set()
        atl=set()
        def dfs(r,c,visit,prevHeight):
            if r<0 or c<0 or (r,c) in visit or r==n or c==m or heights[r][c]<prevHeight:
                return
            visit.add((r,c))
            dfs(r-1,c,visit,heights[r][c])
            dfs(r+1,c,visit,heights[r][c])
            dfs(r,c-1,visit,heights[r][c])
            dfs(r,c+1,visit,heights[r][c])
            
        for i in range(m):
            dfs(0,i,pac,float("-inf"))
            dfs(n-1,i,atl,float("-inf"))
        for i in range(n):
            dfs(i,0,pac,float("-inf"))
            dfs(i,m-1,atl,float("-inf"))
        return list(pac.intersection(atl))