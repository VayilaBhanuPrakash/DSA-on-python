class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        rows = len(grid)
        cols = len(grid[0])

        if (rows + cols - 1) % 2 != 0:
            return False
        
        visited = {}

        def dfs(row,col,bal):

            if bal < 0:
                return False
            
            if row >= rows or col >= cols:
                return False
            
            if grid[row][col] == "(":
                bal += 1
            else:
                bal -= 1

            if bal < 0:
                return False
            
            if row == rows - 1 and col == cols - 1:
                return bal == 0

            state = (row,col,bal)

            if state in visited:
                return visited[state]

            right = dfs(row,col+1,bal)
            down = dfs(row+1,col,bal)

            visited[state] = down or right

            return visited[state]

        return dfs(0,0,0)
            

