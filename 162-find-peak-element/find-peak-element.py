class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        i=0
        j=len(nums)-1
        if j==0:
            return 0
        while i<=j:
            mid=i+(j-i)//2
            if mid==0 and nums[mid]>nums[mid+1]:
                return mid
            elif mid==len(nums)-1 and nums[mid]>nums[mid-1]:
                return mid
            else:
                if nums[mid]>nums[mid+1] and nums[mid]>nums[mid-1]:
                    return mid
                elif nums[mid]>nums[mid+1]:
                    j=mid-1
                else:
                    i=mid+1


        