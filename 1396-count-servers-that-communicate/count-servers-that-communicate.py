class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        rows = [0] * m
        cols = [0] * n
        for i in range(m):
            for j in range(n):
                rows[i] += grid[i][j]
                cols[j] += grid[i][j]
                
        res = 0
        for i in range(m):
            for j in range(n):
                if rows[i] > 1 or cols[j] > 1:
                    res += grid[i][j]
        return res
        