class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        i = 0
        j = 0
        res = 0
        while j < len(nums):
            if nums[i] == 0:
                i += 1
                j = i
            else:
                if nums[j] == 1:
                    j += 1
                else:
                    res = max(res, j - i)
                    i = j + 1
                    j = i
        res = max(res, j - i)
        return res
        