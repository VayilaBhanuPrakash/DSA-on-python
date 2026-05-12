class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        leftmax=[0 for i in range(n)]
        leftmax[0]=height[0]
        for i in range(1,n):
            leftmax[i]=max(leftmax[i-1],height[i])
        rightmax=[0 for i in range(n)]
        rightmax[-1]=height[-1]
        for i in range(n-2,-1,-1):
            rightmax[i]=max(rightmax[i+1],height[i])
        res=0
        for i in range(1,n-1):
            if min(leftmax[i-1],rightmax[i+1])-height[i]>0:
                res=res+min(leftmax[i-1],rightmax[i+1])-height[i]
        return res
        




        