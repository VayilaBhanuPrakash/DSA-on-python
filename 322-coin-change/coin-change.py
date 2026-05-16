class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        rows=len(coins)
        cols=amount
        mtx=[[float('inf') for j in range(cols+1)] for i in range(rows)]
        for i in range(rows):
            for j in range(cols+1):
                if j==0:
                    mtx[i][j]=0
                elif i==0:
                    if j%coins[i]==0:
                        mtx[i][j]=j//coins[i]
                elif coins[i]>j:
                    mtx[i][j]=mtx[i-1][j]
                else:
                    mtx[i][j]=min(mtx[i-1][j],1+mtx[i][j-coins[i]])
            ans=mtx[rows-1][cols]
        return ans if ans!=float('inf') else -1
            



        