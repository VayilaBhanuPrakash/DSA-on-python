class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] = nums[i] & 1
        res = 0
        h = {0 : 1}
        prefix_sum = 0

        for i in range(len(nums)):
            prefix_sum += nums[i]

            required = prefix_sum - k

            if required in h:
                res += h[required]
            
            h[prefix_sum] = h.get(prefix_sum, 0) + 1
        return res
        