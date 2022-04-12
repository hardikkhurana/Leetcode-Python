class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m,n=len(board),len(board[0])
        def valid(a,b):
            return a>=0 and a<m and b>=0 and b<n
        diri=[-1,-1,-1,0,0,+1,+1,+1]
        dirj=[-1,0,+1,-1,+1,-1,0,+1]
        for i in range(m):
            for j in range(n):
                s=0
                for k in range(8):
                    if valid(i+diri[k],j+dirj[k]) and (board[i+diri[k]][j+dirj[k]]==1 or board[i+diri[k]][j+dirj[k]]==-1):
                        s+=1
                if s<2 and board[i][j]==1:
                    board[i][j]=-1
                elif (s==2 or s==3) and board[i][j]==1:
                    board[i][j]=1
                elif s>3 and board[i][j]==1:
                    board[i][j]=-1
                elif s==3 and board[i][j]==0:
                    board[i][j]=2
        for i in range(m):
            for j in range(n):
                if board[i][j]==-1:
                    board[i][j]=0
                if board[i][j]==2:
                    board[i][j]=1
        
        
"""
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m,n=len(board),len(board[0])
        dp=[[0 for j in range(n)]for i in range(m)]
        def valid(a,b):
            return a>=0 and a<m and b>=0 and b<n
        diri=[-1,-1,-1,0,0,+1,+1,+1]
        dirj=[-1,0,+1,-1,+1,-1,0,+1]
        for i in range(m):
            for j in range(n):
                s=0
                for k in range(8):
                    if valid(i+diri[k],j+dirj[k]) and board[i+diri[k]][j+dirj[k]]==1:
                        s+=1
                if (s==2 or s==3) and board[i][j]==1:
                    dp[i][j]=1
                elif s==3 and board[i][j]==0:
                    dp[i][j]=1
        for i in range(m):
            board[i]=dp[i]
"""        