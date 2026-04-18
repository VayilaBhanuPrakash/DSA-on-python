class Solution:
    def mirrorDistance(self, n: int) -> int:
        rev=0
        temp=n
        while temp>0:
            rem=temp%10
            rev=rev*10+rem
            temp//=10
        return abs(rev-n)
        