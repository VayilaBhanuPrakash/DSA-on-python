class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n=len(grid)
        grid2=[[] for i in range(n) ]
        for i in range(n):
            for j in range(n):
                grid2[j].append(grid[i][j])
        h={}
        for ele in grid2:
            t1=tuple(ele)
            if t1 in h:
                h[t1]+=1
            else:
                h[t1]=1
        res=0
        for ele in grid:
            t2=tuple(ele)
            if t2 in h:
                res+=h[t2]
        return res

            


                
            
        