class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        res = 1
        count1 = 1
        count2 = 1
        for i in range(1,len(nums)):
            if nums[i - 1] < nums[i]:
                count1 += 1
                count2 = 1
            elif nums[i - 1] > nums[i]:
                count2 += 1
                count1 = 1
            else:
                count1 = 1
                count2 = 1
            res = max(res,count1,count2)
        return res
        