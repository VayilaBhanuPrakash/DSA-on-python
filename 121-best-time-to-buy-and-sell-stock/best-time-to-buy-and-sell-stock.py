class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy = [0 for _ in range(len(prices))]
        sell = [0 for _ in range(len(prices))]
        buy[0] = prices[0]
        sell[-1] = prices[-1]
        for i in range(1,len(prices)):
            buy[i] = min(buy[i-1],prices[i])
        
        for i in range(len(prices)-1-1,-1,-1):
            sell[i] = max(sell[i+1],prices[i])

        res = 0
        
        for i in range(len(prices)):
            profit = sell[i] - buy[i]
            res = max(res,profit)
        return res


        