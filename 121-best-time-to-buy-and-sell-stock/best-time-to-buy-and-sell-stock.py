class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy = prices[0]
        max_profit = 0
        for ele in prices:
            if buy > ele:
                buy = ele
            else:
                profit = ele - buy
                max_profit = max(max_profit, profit)
        return max_profit




        