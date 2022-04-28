class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        if not heights:
            return 0
        effort=0
        n,m=len(heights),len(heights[0])
        minheap=[(0,0,0)]
        visit=set()
        dir_=[(-1,0),(0,-1),(1,0),(0,1)]
        while minheap:
            w,i,j=heapq.heappop(minheap)
            effort=max(effort,w)
            if (i,j) in visit:
                continue
            if i==n-1 and j==m-1:
                return effort
            visit.add((i,j))
            for p,q in dir_:
                ni,nj=i+p,j+q
                if ni>=0 and nj>=0 and ni<n and nj<m and (ni,nj) not in visit:
                    nw = abs(heights[ni][nj] - heights[i][j])
                    heapq.heappush(minheap, (nw, ni, nj))                
