class Solution:
    def luckyNumbers (self, mat: List[List[int]]) -> List[int]:
        n=len(mat)
        m=len(mat[0])
        r,c=[float("inf") for i in range(n)],[float("-inf") for i in range(m)]
        for i in range(n):
            for j in range(m):
                r[i]=min(r[i],mat[i][j])
                c[j]=max(c[j],mat[i][j])
        res=[]
        for i in range(n):
            for j in range(m):
                if mat[i][j]==r[i]==c[j]:
                    res.append(mat[i][j])
        return res