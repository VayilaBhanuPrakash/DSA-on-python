class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        l = []
        for ele in grid:
            for i in ele:
                l.append(i)
        n = len(l)
        res = []
        k = k % n
        for i in range(n - k,n):
            res.append(l[i])
        for i in range(n-k):
            res.append(l[i])
        k = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                grid[i][j] = res[k]
                k += 1
        return grid



        