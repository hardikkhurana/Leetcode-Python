class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        n,m=len(board),len(board[0])
        res=0
        for i in range(n):
            for j in range(m):
                if board[i][j]=="X":
                    if i==0 and j==0:
                        res+=1
                    elif i==0:
                        if board[i][j-1]!="X":
                            res+=1                            
                    elif j==0:
                        if board[i-1][j]!="X":
                            res+=1     
                    else:
                        if board[i][j-1]!="X" and board[i-1][j]!="X":
                            res+=1     
                        
        return res
        