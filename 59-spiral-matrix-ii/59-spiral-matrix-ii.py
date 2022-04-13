class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat=[[0 for i in range(n)] for j in range(n)]
        l,r,t,b=0,n-1,0,n-1
        val=1
        while l<=r:
            for i in range(l,r+1):
                mat[t][i]=val
                val+=1
            t+=1
            for i in range(t,b+1):
                mat[i][r]=val
                val+=1
            r-=1
            for i in range(r,l-1,-1):
                mat[b][i]=val
                val+=1
            b-=1
            for i in range(b,t-1,-1):
                mat[i][l]=val
                val+=1
            l+=1
        return mat
            
        