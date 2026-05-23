class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n=len(grid)
        grid2=[[] for i in range(n) ]
        for i in range(n):
            for j in range(n):
                grid2[j].append(grid[i][j])
        res=0
        for ele in grid:
            if ele in grid2:
                res+=grid2.count(ele)
        return res

        
            
        