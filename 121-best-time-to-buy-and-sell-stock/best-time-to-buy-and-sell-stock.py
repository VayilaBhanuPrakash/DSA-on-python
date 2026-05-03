class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice=float('inf')
        maxprofit=0
        for ele in prices:
            if ele<minprice:
                minprice=ele
            else:
                profit=ele-minprice
                maxprofit=max(maxprofit,profit)
        return maxprofit
        