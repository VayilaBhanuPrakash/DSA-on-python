class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        h = {0 : -1}
        prefix = 0
        s = {0}
        for i in range(len(nums)):
            prefix += nums[i]
            if prefix % k in s and i - h[prefix % k] >= 2:
                return True
            if prefix % k not in h:
                h[prefix % k] = i
                s.add(prefix % k)
        return False
        