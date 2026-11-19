class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy = prices[0]
        res = 0
        for ele in prices:
            res = max(res, ele - buy)
            buy = min(buy, ele)
        return res




        