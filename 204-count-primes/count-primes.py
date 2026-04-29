class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=2:
            return 0
        prime=[True]*n
        prime[0]=prime[1]=False
        for i in range(1,int(n**0.5)+1):
            if prime[i]:
                for j in range(i**2,n,i):
                    prime[j]=False
        return sum(prime)
        """count=1
        for i in range(3,n,2):
            flag=True
            j=3
            while j*j<=i:
                if i%j==0:
                    flag=False
                    break
                j+=2
            if flag:
                count+=1
        return count"""

        