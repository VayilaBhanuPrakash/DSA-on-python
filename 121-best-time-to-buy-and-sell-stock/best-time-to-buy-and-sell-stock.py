class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy = prices[0]
        res = 0
        for ele in prices:
            if ele < buy:
                buy = ele
            else:
                res = max(res, ele - buy)
        return res




        