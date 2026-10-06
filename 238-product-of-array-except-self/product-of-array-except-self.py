class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        preprod = [0 for _ in range(n)]
        preprod[0] = nums[0]
        for i in range(1,n):
            preprod[i] = preprod[i-1] * nums[i]

        sufprod = [0 for _ in range(n)]
        sufprod[n-1] = nums[n-1]
        for i in range(n-1-1,-1,-1):
            sufprod[i] = sufprod[i+1] * nums[i]
        
        nums[0] = sufprod[1]
        nums[n-1] = preprod[n-2]
        for i in range(1,n-1):
            nums[i] = preprod[i-1] * sufprod[i+1]
        return nums
        
        

        