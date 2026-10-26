class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        res = 0

        def  dfs(row,col):
            nonlocal count
            count += 1
            grid[row][col] = 0

            dirs = ((1,0),(-1,0),(0,1),(0,-1))
            for r,c in dirs:
                roww = row + r
                coll = col + c
                if roww >= 0 and roww < rows and coll >= 0 and coll < cols and grid[roww][coll] == 1:
                    dfs(roww,coll)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    count = 0
                    dfs(i,j)
                    res = max(res,count)
        return res

















        