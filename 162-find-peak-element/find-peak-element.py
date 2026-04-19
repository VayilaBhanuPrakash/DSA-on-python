class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """index=0
        Peak=nums[0]
        for i in range(1,len(nums)):
            if nums[i]>Peak:
                Peak=nums[i]
                index=i
        return index"""
        n=len(nums)
        if n==1:
            return 0
        for i in range(n):
            if i==0:
                if i+1<=n-1 and nums[i]>nums[i+1]:
                    return i
            elif i==n-1:
                if nums[i]>nums[i-1]:
                    return i
            else:
                if nums[i]>nums[i-1] and nums[i]>nums[i+1]:
                    return i
        return -1
            
        