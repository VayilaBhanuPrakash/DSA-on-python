class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        rows = set()
        cols = set()
        for i in range(len(grid)):
            if sum(grid[i]) > 1:
                rows.add(i)
        for j in range(len(grid[0])):
            summ = 0
            for i in range(len(grid)):
                summ += grid[i][j]
            
            if summ > 1:
                cols.add(j)
        
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i in rows or j in cols:
                    res += grid[i][j]
        return res
        