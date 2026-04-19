class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        index=0
        Peak=nums[0]
        for i in range(1,len(nums)):
            if nums[i]>Peak:
                Peak=nums[i]
                index=i
        return index
        