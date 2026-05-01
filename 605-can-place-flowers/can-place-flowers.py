class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """nn=len(flowerbed)
        if nn==1:
            if n==0:
                return True
            elif flowerbed[0]==0 and n==1:
                return True
            elif flowerbed[0]==1 and n>=1:
                return False
        
        for i in range(nn):
            if (i==0 and flowerbed[i]==0 and flowerbed[i+1]==0 and n>0):
                flowerbed[i]=1
                n-=1
            elif (i==nn-1 and flowerbed[i]==0 and flowerbed[i-1]==0 and n>0):
                flowerbed[i]=1
                n-=1
            elif (i>0 and i<nn-1) and flowerbed[i]==0 and flowerbed[i-1]==0 and flowerbed[i+1]==0 and n>0:
                flowerbed[i]=1
                n-=1
        return n==0"""

































        count=0
        n1=len(flowerbed)
        for i in range(n1):
            if flowerbed[i]==0 and (((i==0) or (flowerbed[i-1]==0)) and ((i==n1-1) or (flowerbed[i+1]==0))):
                flowerbed[i]=1
                count+=1
                if count>=n:
                    return True
        return count>=n

        