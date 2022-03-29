class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        origin_color = grid[row][col]
        m = len(grid)
        n = len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = deque([(row, col)])
        seen = set()
        seen.add((row, col))
        while q:
            i, j = q.popleft()
            if (i == 0 or i == m - 1 or j == 0 or j == n - 1) and grid[i][j] == origin_color:
                grid[i][j] = color
            for d in directions:
                new_i, new_j = i + d[0], j + d[1]
                if 0 <= new_i < m and 0 <= new_j < n and (new_i, new_j) not in seen:
                    if grid[new_i][new_j] == origin_color:
                        q.append((new_i, new_j))
                        seen.add((new_i, new_j))
                    else:
                        grid[i][j] = color
                        
        return grid