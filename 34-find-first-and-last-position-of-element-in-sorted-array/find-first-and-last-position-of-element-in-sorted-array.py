class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res=[-1,-1]
        if len(nums)==0:
            return res
        i=0
        j=len(nums)-1
        while i<=j:
            mid=i+(j-i)//2
            if nums[mid]==target:
                left=mid
                right=mid
                while left>=0 and nums[left]==target:
                    left-=1
                res[0]=left+1
                while right<=len(nums)-1 and nums[right]==target:
                    right+=1
                res[1]=right-1
                return res
            elif nums[mid]>target:
                j=mid-1
            else:
                i=mid+1
        return res
        