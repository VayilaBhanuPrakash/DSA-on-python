class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        h = {0 : 1}
        prefix_sum = 0
        res  = 0
        for ele in nums:
            prefix_sum += ele
            required = prefix_sum - goal

            if required in h:
                res += h[required]
            
            h[prefix_sum] = h.get(prefix_sum, 0) + 1

        return res
        