class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy = prices[0]
        max_profit = 0

        for ele in prices:
            if ele < buy:
                buy = ele
            else:
                profit = ele - buy
                max_profit = max(profit,max_profit)
        return max_profit



        