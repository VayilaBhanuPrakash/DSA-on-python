class Solution:
    def isHappy(self, n: int) -> bool:
        s=set()
        while n>0 and n not in s:
            s.add(n)
            sum=0
            while n>0:
                r=n%10
                sum=sum+r**2
                n=n//10
            n=sum
        return sum==1

        