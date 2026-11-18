class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix = 0
        h = {0 : -1}
        res = 0
        for i in range(len(nums)):
            val = nums[i] if nums[i] else -1
            prefix += val
            if prefix not in h:
                h[prefix] = i
            else:
                res = max(res,i - h[prefix])
        if prefix in h:
            res = max(res, len(nums) - h[prefix] - 1)

        return res
        