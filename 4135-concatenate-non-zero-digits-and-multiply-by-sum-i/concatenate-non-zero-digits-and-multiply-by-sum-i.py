class Solution:
    def sumAndMultiply(self, n: int) -> int:
        res = 0
        summ = 0
        temp = n
        while temp != 0:
            rem = temp % 10
            temp = temp // 10
            summ += rem
            if rem != 0:
                res = res * 10 + rem
        print(res)
        ress = 0
        while res != 0:
            rem = res % 10
            res = res // 10
            ress = ress * 10 + rem
        return ress * summ


        