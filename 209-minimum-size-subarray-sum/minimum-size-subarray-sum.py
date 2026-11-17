class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        res = len(nums) + 1
        summ = nums[0]
        left = 0
        right = 1
        if summ >= target:
            return 1
        while right < len(nums):
            summ += nums[right]
            
            if summ >= target:
                res = min(res, right - left + 1)
                right += 1
                while summ >= target:
                    summ -= nums[left]
                    left += 1
                    res = min(res, right - left + 1)
            else:
                right += 1
                    
        if res > len(nums):
            return 0
        return res

        