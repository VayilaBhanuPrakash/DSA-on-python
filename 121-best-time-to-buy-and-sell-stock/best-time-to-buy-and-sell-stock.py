class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        m=[0]*n
        m[0]=prices[0]
        for i in range(1,n):
            m[i]=min(prices[i],m[i-1])
        res=0
        for i in range(1,n):
            res=max(res,prices[i]-m[i-1])
        return res
            

        