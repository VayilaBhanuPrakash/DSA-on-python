class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        res = 0
        i = 0
        count = 0
        for j in range(len(nums)):
            if nums[j] == 0:
                count += 1
            while count > 1:
                if nums[i] == 0:
                    count -=1
                i += 1
            res = max(res, j - i)
        return res
        