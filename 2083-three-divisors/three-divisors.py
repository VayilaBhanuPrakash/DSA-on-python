class Solution:
    def isThree(self, n: int) -> bool:
        i=1
        count=0
        while i<=n//2:
            if n%i==0:
                count+=1
            i+=1
        return count==2

        