class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        m=[0 for i in range(n)]
        m[0]=prices[0]
        for i in range(1,n):
            m[i]=min(prices[i],m[i-1])
        print(m)
        res=float('-inf')
        for i in range(1,n):
            res=max(res,prices[i]-m[i-1])
        if res>0:
            return res
        return 0
            

        