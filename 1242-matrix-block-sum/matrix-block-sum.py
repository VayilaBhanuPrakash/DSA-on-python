class Solution:
    def matrixBlockSum(self, mat: list[list[int]], k: int) -> list[list[int]]:
       rows = len(mat)
       cols = len(mat[0])

       prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
       
       for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            prefix[i][j] = mat[i - 1][j - 1] + prefix[i -1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1]

       ans = [[0] * (cols) for _ in range(rows)]

       for i in range(rows):
        for j in range(cols):
            r1 = max(0, i - k)
            c1 = max(0, j - k)
            r2 = min(rows - 1, i + k)
            c2 = min(cols - 1, j + k)
            r1 += 1
            r2 += 1
            c1 += 1
            c2 += 1

            ans[i][j] = prefix[r2][c2] - prefix[r1 - 1][c2] - prefix[r2][c1 - 1] + prefix[r1 -1][c1 - 1]
       return ans 



             

        