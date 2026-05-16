class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i=0
        j=len(nums)-1
        while i<=j:
            mid=i+(j-i)//2
            if nums[mid]==target:
                return mid
            if nums[i]<=nums[mid]:
                if nums[i]<=target and target<=nums[mid]:
                    j=mid-1
                else:
                    i=mid+1
            if nums[j]>=nums[mid]:
                if nums[mid]<=target and target<=nums[j]:
                    i=mid+1
                else:
                    j=mid-1
        return -1
            
           