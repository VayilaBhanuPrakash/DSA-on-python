class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        rows=len(coins)
        coins.sort()
        cols=amount
        mtx=[[0 for j in range(cols+1)] for i in range(rows)]
        for i in range(rows):
            for j in range(cols+1):
                if j==0:
                    mtx[i][j]=1
                elif i==0:
                    if j%coins[i]==0:
                        mtx[i][j]=1
                elif coins[i]>j:
                    mtx[i][j]=mtx[i-1][j]
                else:
                    mtx[i][j]=mtx[i-1][j]+mtx[i][j-coins[i]]
        return mtx[rows-1][cols]
        