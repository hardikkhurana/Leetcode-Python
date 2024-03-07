class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n,m = len(board), len(board[0])
        rows = defaultdict(set)
        col = defaultdict(set)
        box = defaultdict(set)
        
        for i in range(n):
            for j in range(m):
                val = board[i][j]
                if val == ".":
                    continue
                if val in rows[i]:
                    return False
                if val in col[j]:
                    return False
                if val in box[(i//3,j//3)]:
                    return False
                rows[i].add(val)
                col[j].add(val)
                box[(i//3,j//3)].add(val)
        return True
[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9",
