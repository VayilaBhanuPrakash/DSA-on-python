class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        rows = len(grid)
        cols = len(grid[0])

        if (rows + cols - 1 ) % 2 != 0:
            return False
        
        memo = {}

        def dfs(row,col,bal):

            if bal < 0:
                return False
            if row >= rows or col >= cols:
                return False
            
            if grid[row][col] == '(':
                bal += 1
            else:
                bal -= 1
            
            if bal < 0:
                return False

            state = (row,col,bal)
            if state in memo:
                return memo[state]
            
            if row == rows - 1 and col == cols - 1:
                return bal == 0

            down = dfs(row + 1,col,bal)
            right = dfs(row,col + 1,bal)

            memo[state] = down or right

            return memo[state]
        return dfs(0,0,0)
            


        