class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        m = max(costs)
        c = [0] * (m+1)
        for ele in costs:
            c[ele] += 1
        result = []
        for i in range(len(c)):
           result.extend([i] * c[i])
        res = 0
        buy = 0
        for ele in result:
            buy += ele
            if buy > coins:
                break
            res += 1
        return res


        