class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        m = max(costs)
        c = [0] * (m+1)
        for ele in costs:
            c[ele] += 1
        res = 0
        for price in range(m+1):
            if c[price] == 0:
                continue
            if coins < price:
                break
            for i in range(c[price]):
                if coins >= price:
                    coins -= price
                    res += 1
                else:
                    break
        return res


            
           


        