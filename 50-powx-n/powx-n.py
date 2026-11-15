class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        base = x
        if n > 0:
            while n:
                if n & 1:
                    res = res * base
                n = n >> 1
                base = base * base
            return res
        else:
            n = -n
            while n:
                if n & 1:
                    res = res / base
                n = n >> 1
                base = base * base
            return res