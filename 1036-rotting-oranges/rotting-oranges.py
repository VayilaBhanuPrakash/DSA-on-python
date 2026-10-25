class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        flag = 1
        time = 0
        while True:
            if flag == 0:
                break
            flag = 0
            for i in range(rows):
                for j in range(cols):
                    if grid[i][j] == 2:
                        if i - 1 >= 0 and grid[i-1][j] == 1:
                            grid[i-1][j] = 3
                        if i + 1 < rows and grid[i+1][j] == 1:
                            grid[i+1][j] = 3
                        if j - 1 >= 0 and grid[i][j-1] == 1:
                            grid[i][j-1] = 3
                        if j + 1 < cols and grid[i][j+1] == 1:
                            grid[i][j+1] = 3
            for i in range(rows):
                for j in range(cols):
                    if grid[i][j] == 3:
                        grid[i][j] = 2
                        flag = 1
            if flag == 1:
                time += 1
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1
                    
        return time
        