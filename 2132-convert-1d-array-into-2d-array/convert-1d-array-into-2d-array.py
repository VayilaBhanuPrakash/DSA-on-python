class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        length=len(original)
        if length!=m*n:
            return []
        res=[[0 for i in range(n)] for j in range(m)]
        for i in range(length):
            row=i//n
            col=i%n
            res[row][col]=original[i]
        return res
