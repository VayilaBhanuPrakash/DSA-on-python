class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        if n==1 and nums[0]==target:
            return 0
        i=0
        j=n-1
        pivot=-1
        while i<=j:
            mid=i+(j-i)//2
            if mid+1<n and nums[mid]>nums[mid+1]:
                pivot=mid
                break
            elif nums[i]<=nums[mid]:
                i=mid+1
            else:
                j=mid-1
        print(pivot)
        i=0
        j=pivot
        while i<=j:
            mid=i+(j-i)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                i=mid+1
            else:
                j=mid-1
        i=pivot+1
        j=n-1
        while i<=j:
            mid=i+(j-i)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                i=mid+1
            else:
                j=mid-1
        return -1

        """i=0
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
        return -1"""

            
           