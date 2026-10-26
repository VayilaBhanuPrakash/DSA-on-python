class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        rows = len(grid)
        cols = len(grid[0])
    
        def dfs(row,col):
            sum = grid[row][col]
            grid[row][col] = 0

            if row - 1 >= 0 and col >= 0 and row - 1 < rows and col < cols and grid[row-1][col] > 0:
                sum +=  dfs(row-1,col)
            if row + 1 >= 0 and col >= 0 and row + 1 < rows and col < cols and grid[row+1][col] > 0:
                sum +=  dfs(row+1,col)
            if row >= 0 and col - 1 >= 0 and row < rows and col - 1 < cols and grid[row][col-1] > 0:
                sum +=  dfs(row,col-1)
            if row >= 0 and col + 1 >= 0 and row < rows and col + 1 < cols and grid[row][col+1] > 0:
                sum +=  dfs(row,col+1)
            
            return sum
            
        res = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] != 0:
                    if dfs(i,j) % k == 0:
                        res += 1
        return res


        