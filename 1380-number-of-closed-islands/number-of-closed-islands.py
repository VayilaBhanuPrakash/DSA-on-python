class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        def dfs(row,col):
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return False
            if grid[row][col] == 1:
                return True
            grid[row][col] = 1

            up = dfs(row + 1, col)
            down = dfs(row - 1, col)
            right = dfs(row, col + 1)
            left = dfs(row, col - 1)
            return up and down and right and left

        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    if dfs(i,j):
                        count += 1
        return count 
        