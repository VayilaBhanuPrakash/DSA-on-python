class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n=len(nums)
        if n==1 and nums[0]==target:
            return True
        i=0
        j=n-1
        pivot=-1
        while i<=j:
            mid=i+(j-i)//2
            if mid<j and nums[mid]>nums[mid+1]:
                pivot=mid
                break
            if mid>i and nums[mid]<nums[mid-1]:
                pivot=mid-1
                break
            if nums[i]==nums[mid]==nums[j]:
                if i<j and nums[i]>nums[i+1]:
                    pivot=i
                    break
                i+=1
                if j>i and nums[j-1]>nums[j]:
                    pivot=j-1
                    break
                j-=1
            elif nums[i]<=nums[mid]:
                i=mid+1
            else:
                j=mid-1
        i=0
        j=pivot
        while i<=j:
            mid=i+(j-i)//2
            if nums[mid]==target:
                return True
            elif nums[mid]<target:
                i=mid+1
            else:
                j=mid-1
        i=pivot+1
        j=n-1
        while i<=j:
            mid=i+(j-i)//2
            if nums[mid]==target:
                return True
            elif nums[mid]<target:
                i=mid+1
            else:
                j=mid-1
        return False