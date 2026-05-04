class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l=[rows[:] for rows in matrix]
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                matrix[i][j]=l[len(matrix)-1-j][i]
        return matrix
        