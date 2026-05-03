class Solution:
    def sumOfPrimesInRange(self, n: int) -> int:
        def isprime(n):
            if n<2:
                return False
            j=2
            while j*j<=n:
                if n%j==0:
                    return False
                j+=1
            return True
        temp=n
        rev=0
        while temp>0:
            rem=temp%10
            temp=temp//10
            rev=rev*10+rem
        if n>rev:
            start=rev
            end=n
        else:
            start=n
            end=rev
        res=0
        for i in range(start,end+1):
            if isprime(i):
                res=res+i
        return res
        