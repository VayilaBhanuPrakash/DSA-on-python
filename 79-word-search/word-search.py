class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])

        def dfs(i,j,k=0):
            if k == len(word):
                return True
            if not (i>=0 and j>=0 and i<n and j<m):
                return False
            if board[i][j] != word[k]:
                return False
            board[i][j] = '!'

            if dfs(i+1,j,k+1) or dfs(i-1,j,k+1) or dfs(i,j+1,k+1) or dfs(i,j-1,k+1):
                return True
            board[i][j] = word[k]
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    if dfs(r,c):
                        return True
        return False
