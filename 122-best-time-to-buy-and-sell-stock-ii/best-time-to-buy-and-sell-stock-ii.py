class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res=0
        n=len(prices)
        i,j=0,1
        while j<n:
            if prices[i]<prices[j]:
                a=prices[i]
                while j<n and prices[i]<prices[j]:
                    profit=prices[j]-a
                    i+=1
                    j+=1
                res=res+profit
            i+=1
            j+=1
        return res

        