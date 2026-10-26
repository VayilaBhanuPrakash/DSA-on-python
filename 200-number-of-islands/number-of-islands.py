class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        res = 0
        def dfs(roww,coll):
            grid[roww][coll] = '0'

            dir = ((1,0),(0,1),(-1,0),(0,-1))
            for r,c in dir:
                row = roww + r
                col = coll + c

                if row >= 0 and col >= 0 and row < rows and col < cols and grid[row][col] == '1':
                    dfs(row,col)
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    res += 1
                    dfs(i,j)
        return res

        