class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        count = 0
        h = {0 : 1}

        for ele in nums:
            prefix_sum += ele

            if prefix_sum - k in h:
                count += h[prefix_sum - k]
            if prefix_sum in h:
                h[prefix_sum] += 1
            else:
                h[prefix_sum] = 1
        return count




        