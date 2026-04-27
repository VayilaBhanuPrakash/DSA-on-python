class Solution:
    def findComplement(self, num: int) -> int:
        i=0
        res=0
        while num>0:
            rem=num%2
            num=num//2
            if rem==0:
                res+=2**i
            else:
                pass
            i+=1
        return res

        