class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(i,j,k):
            if (i < 0 or j < 0 or i >= row or j >= col):
                return False
            if board[i][j] != word[k]:
                return False
            if board[i][j] == word[k] and k == len(word) - 1:
                return True
            board[i][j] = "!"

            if dfs(i+1,j,k+1) or dfs(i-1,j,k+1) or dfs(i,j+1,k+1) or dfs(i,j-1,k+1):
                return True

            board[i][j] = word[k]

        row=len(board)
        col=len(board[0])
        for rows in range(row):
            for cols in range(col):
                if board[rows][cols]==word[0] and dfs(rows,cols,0):
                    return True
        return False
                    
        