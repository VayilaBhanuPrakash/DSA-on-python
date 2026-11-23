class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxx = float('-inf')
        prefix = 0
        for i in range(len(nums)):
            prefix += nums[i]
            prefix = max(prefix,nums[i])
            maxx = max(maxx,prefix)
        return maxx