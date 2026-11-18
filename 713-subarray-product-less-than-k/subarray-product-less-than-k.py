class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        res = 0
        i = 0
        product = 1
        for j in range(len(nums)):
            product = product * nums[j]
            while i < j and product >= k:
                product = product // nums[i]
                i += 1
            if product < k:
                res = res + j - i + 1
        return res



        