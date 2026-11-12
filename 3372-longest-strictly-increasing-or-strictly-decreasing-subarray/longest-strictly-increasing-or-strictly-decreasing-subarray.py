class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        res = 1
        count1 = 1
        count2 = 1
        num = nums[0]
        for i in range(1,len(nums)):
            if nums[i] > num:
                count1 += 1
                res = max(res,count1)
                count2 = 1
            elif nums[i] < num:
                count2 += 1
                res = max(res,count2)
                count1 = 1
            else:
                count1 = 1
                count2 = 1
            num = nums[i]
        res = max(res,count1)
        res = max(res,count2)
        return res
        