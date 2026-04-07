class Solution:
    def checkDivisibility(self, n: int) -> bool:
        Product=1
        Sum=0
        temp=n
        while temp>0:
            rem=temp%10
            Sum+=rem
            Product*=rem
            temp=temp//10
        return n%(Product+Sum)==0
        