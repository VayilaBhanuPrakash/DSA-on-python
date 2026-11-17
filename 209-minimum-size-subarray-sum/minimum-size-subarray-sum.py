class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        res = float('inf')
        summ = nums[0]
        left = 0
        right = 1
        flag = False
        if summ >= target:
            return 1
        while left < right and right < len(nums):
            summ += nums[right]
            
            if summ >= target:
                res = min(res, right - left + 1)
                flag = True
                right += 1
                while summ >= target:
                    summ -= nums[left]
                    left += 1
                    res = min(res, right - left + 1)
            else:
                right += 1
                    
        if not flag:
            return 0
        return res

        