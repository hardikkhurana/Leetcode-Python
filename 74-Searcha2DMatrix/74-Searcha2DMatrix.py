[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n=len(matrix)
        m=len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==target:
                    return True

        return False  
