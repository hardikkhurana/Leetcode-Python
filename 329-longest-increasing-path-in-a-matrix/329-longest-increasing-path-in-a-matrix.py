class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp={}
        R,C=len(matrix),len(matrix[0])
        
        def dfs(r,c,prevVal):
            if r<0 or c<0 or r==R or c==C or matrix[r][c]<=prevVal:
                return 0
            if (r,c) in dp:
                return dp[(r,c)]
            res=1
            res=max(res,1+dfs(r+1,c,matrix[r][c]))
            res=max(res,1+dfs(r-1,c,matrix[r][c]))
            res=max(res,1+dfs(r,c+1,matrix[r][c]))
            res=max(res,1+dfs(r,c-1,matrix[r][c]))
            dp[(r,c)]=res
            return res
        
        LIP=0
        for i in range(R):
            for j in range(C):
                LIP=max(LIP,dfs(i,j,-1))
        return LIP
        