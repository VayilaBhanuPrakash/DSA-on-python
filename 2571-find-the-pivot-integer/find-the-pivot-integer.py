class Solution:
    def pivotInteger(self, n: int) -> int:
        summ=(n*(n+1))/2
        first_sum=0
        for i in range(1,n+1):
            first_sum+=i
            if first_sum==summ:
                return i
            summ-=i
        return -1
        