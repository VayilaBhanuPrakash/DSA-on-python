class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        fresh = 0
        rotten = []
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    rotten.append([i,j])
                elif grid[i][j] == 1:
                    fresh += 1
        if not fresh:
            return 0
        flag = 1
        res = 0
        while fresh and flag:
            flag = 0
            new_rotten = []
            for i in range(rows):
                for j in range(cols):
                    if grid[i][j] == 1 and ([i-1,j] in rotten or [i+1,j] in rotten or [i,j-1] in rotten or [i,j+1] in rotten):
                        grid[i][j] = 2
                        flag = 1
                        fresh -= 1
                        new_rotten.append([i,j])
            rotten.extend(new_rotten)
            res += 1
        return -1 if fresh else res
        