class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        lowest = [0] * len(prices)
        lowest[0] = prices[0]
        for i in range(1,len(prices)):
            lowest[i] = min(lowest[i - 1], prices[i])
        res = 0
        for i in range(len(prices)):
            res = max(res, prices[i] - lowest[i])
        return res




        