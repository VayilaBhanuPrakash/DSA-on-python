class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        res = n + 1
        summ = 0
        left = 0

        for right in range(n):
            summ += nums[right]
            
            while summ >= target:
                res = min(res, right - left + 1)
                if res == 1:
                    return 1
                summ -= nums[left]
                left += 1
                 
        return 0 if res > n else res
        