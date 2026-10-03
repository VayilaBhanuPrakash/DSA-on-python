class Solution:
    def uniquePathsWithObstacles(self, grid: list[list[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        mat = [[0] * col for _ in range(row)]
        
        for i in range(row-1,-1,-1):
            if grid[i][col-1] == 1:
                break
            else:
                mat[i][col-1] = 1
        for j in range(col-1,-1,-1):
            if grid[row-1][j] == 1:
                break
            else:
                mat[row-1][j] = 1


        for i in range(row-1-1,-1,-1):
            for j  in range(col-1-1,-1,-1):
                if grid[i][j] == 1:
                    continue
                else:
                    mat[i][j] = mat[i+1][j] + mat[i][j+1]

                    
        return mat[0][0]
                



        
        
        