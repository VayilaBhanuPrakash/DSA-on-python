class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        res = 0
        left = 0
        product = 1
        for right in range(len(nums)):
            product = product * nums[right]
            while left < right and product >= k:
                product //= nums[left]
                left += 1
            if product < k:
                res += right - left + 1
        return res




        