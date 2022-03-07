class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        n=len(matrix)
        m=len(matrix[0])
        ans=0
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==1:
                    if i==0 or j==0:
                        ans+=1
                    else:
                        matrix[i][j]=min(matrix[i-1][j],matrix[i][j-1],matrix[i-1][j-1])+1
                        ans+=matrix[i][j]
        return ans
        
        