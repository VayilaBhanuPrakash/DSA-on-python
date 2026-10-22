class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        left = 0
        right = x + 1
        while left <= right:
            mid = (left + right)//2
            val1 = mid * mid
            val2 = (mid+1) * (mid+1)
            if val1 == x:
                return mid
            if val1 < x and x < val2:
                return mid
            elif val2 > x:
                right = mid - 1
            else:
                left = mid + 1
        