class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        fresh = 0
        rotten = []
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    rotten.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1
        flag = 1
        res = 0
        while fresh and flag:
            flag = 0
            dirs = ((1,0),(-1,0),(0,1),(0,-1))
            n = len(rotten)
            for i in range(n):
                rott = rotten.pop(0)
                for row,col in dirs:
                    roww = row + rott[0]
                    coll = col + rott[1]
                    if roww >= 0 and roww < rows and coll >= 0 and coll < cols and grid[roww][coll] == 1:
                        grid[roww][coll] = 2
                        rotten.append((roww,coll))
                        fresh -= 1
                        flag = 1
            res += 1

        return -1 if fresh else res
            

  
        
        