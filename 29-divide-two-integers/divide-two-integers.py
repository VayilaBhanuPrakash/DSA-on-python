class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        max=2**32-1
        if (dividend>0 and divisor>0) or (dividend<0 and divisor<0):
            val=dividend//divisor
        else:
            val=ceil(dividend/divisor)
        if val>2**31-1:
            return 2**31-1
        else:
            return val
            
            
        