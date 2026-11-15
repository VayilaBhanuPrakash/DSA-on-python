class Solution:
    def getSum(self, a: int, b: int) -> int:
        if a > 0 and b > 0:
            while a != 0 and b != 0:
                temp1 = a
                temp2 = b
                a = temp1 ^ temp2
                b = (temp1 & temp2) << 1
            return a ^ b
        else:
            mask = 0xFFFFFFFF
            while b != 0:
                carry = ((a & b) << 1) & mask
                a = (a ^ b) & mask
                b = carry
            if a >= (1 << 31):
                a = ~(a ^ mask)
            return a

    
