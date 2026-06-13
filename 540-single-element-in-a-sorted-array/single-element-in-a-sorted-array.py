class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        i = 0
        j = len(nums)
        if j == 1:
            return nums[0]
        while i <= j:
            mid = i + (j-i)//2
            if mid - 1 >= 0 and mid + 1 < len(nums) and nums[mid] != nums[mid+1] and nums[mid] != nums[mid-1]:
                return nums[mid]
            if mid % 2 ==0 :
                if mid + 1 < len(nums) and nums[mid] == nums[mid+1]:
                    i = mid + 1
                else:
                    j = mid - 1
            else:
                if mid - 1 >= 0 and nums[mid] == nums[mid-1]:
                    i = mid + 1
                else:
                    j = mid - 1
        if mid == len(nums)-2:
            return nums[-1]
        return nums[mid]

        