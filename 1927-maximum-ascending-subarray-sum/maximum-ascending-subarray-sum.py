class Solution:
    def maxAscendingSum(self, nums: list[int]) -> int:
        res = nums[0]
        ans = nums[0]
        for i in range(1,len(nums)):
            if nums[i-1] < nums[i]:
                res += nums[i]
            else:
                ans = max(ans,res)
                res = nums[i]
        return max(ans,res)
        