class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l=[rows[:] for rows in matrix]
        n=len(l)
        m=len(l[0])
        for i in range(n):
            for j in range(m):
                if l[i][j]==0:
                    for cols in range(m):
                        matrix[i][cols]=0
                    for rows in range(n):
                        matrix[rows][j]=0
        