class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        preProd=[0 for i in range(n)]
        prod=1
        for i in range(n):
            prod=prod*nums[i]
            preProd[i]=prod
        sufProd=[0 for i in range(n)]
        prod=1
        for i in range(n-1,-1,-1):
            prod=prod*nums[i]
            sufProd[i]=prod
        nums[0]=sufProd[1]
        nums[n-1]=preProd[n-2]
        for i in range(1,n-1):
            nums[i]=preProd[i-1]*sufProd[i+1]
        return nums

        