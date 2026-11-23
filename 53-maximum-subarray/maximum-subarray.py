class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxx = float('-inf')
        prefix = 0
        for i in range(len(nums)):
            prefix = max(prefix + nums[i],nums[i])
            maxx = max(maxx,prefix)
        return maxx