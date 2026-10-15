class Solution:
    def maxAscendingSum(self, nums: list[int]) -> int:
        res = 0
        ans = 0
        for i in range(len(nums)):
            if res == 0:
                res += nums[i]
            else:
                if nums[i-1] < nums[i]:
                    res += nums[i]
                else:
                    res = nums[i]
            ans = max(ans,res)
        return ans
            
        