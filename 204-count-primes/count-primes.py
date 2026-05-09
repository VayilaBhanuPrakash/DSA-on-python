class Solution:
    def countPrimes(self, n: int) -> int:
        if n<2:
            return 0
        a=[True for i in range(n)]
        a[0]=a[1]=False
        for i in range(2,n+1):
            for j in range(i+i,n,i):
                a[j]=False
        count=0
        for i in range(n):
            if a[i]==True:
                count+=1
        return count
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

        