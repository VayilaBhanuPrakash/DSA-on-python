class Solution:
    def maxArea(self, nums: list[int]) -> int:
        left = 0
        right = len(nums) - 1
        res = 0
        while left < right:
            res = max(res,(right - left) * min(nums[left],nums[right]))

            if nums[left] < nums[right]:
                left += 1
            else:
                right -= 1
        return res
            

        



        
        