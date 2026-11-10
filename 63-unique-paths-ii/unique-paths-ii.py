class Solution:
    def uniquePathsWithObstacles(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        mat = [[0] * n for _ in range(m)]

        for i in range(m):
            if grid[i][0] == 1:
                break
            mat[i][0] = 1
        
        for j in range(n):
            if grid[0][j] == 1:
                break
            mat[0][j] = 1
        
        for i in range(1,m):
            for j in range(1,n):
                if grid[i][j] == 1:
                    continue
                mat[i][j] = mat[i-1][j] + mat[i][j-1]
        return mat[m-1][n-1]
                



        
        