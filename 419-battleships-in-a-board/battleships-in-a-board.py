class Solution:
    def countBattleships(self, board: list[list[str]]) -> int:
        rows = len(board)
        cols = len(board[0])
        res = 0

        def  dfs(row,col):
            board[row][col] = "."

            dirs = ((1,0),(0,1))
            for r,c in dirs:
                roww = row + r
                coll = col + c
                if roww >= 0 and roww < rows and coll >= 0 and coll < cols and board[roww][coll] == "X":
                    dfs(roww,coll)
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "X":
                    dfs(i,j)
                    res += 1
        return res
        