class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        n = len(nums)
        left = 0
        res = n + 1
        summ = 0
        if max(nums) >= target:
            return 1
        for right in range(n):
            summ += nums[right]
            while summ >= target:
                res = min(res, right - left + 1)
                summ -= nums[left]
                left += 1
        return 0 if res == n + 1 else res
            
            
        

        