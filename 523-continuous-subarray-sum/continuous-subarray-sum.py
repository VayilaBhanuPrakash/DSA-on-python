class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        h = {0 : -1}
        prefix = 0
        for i in range(len(nums)):
            prefix += nums[i]
            r = prefix % k
            if r in h:
                if i - h[prefix % k] >= 2:
                    return True
            else:
                h[r] = i
        return False
        