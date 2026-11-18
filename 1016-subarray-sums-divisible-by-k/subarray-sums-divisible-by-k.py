class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        res = 0
        h = {0 : 1}
        prefix = 0
        for ele in nums:
            prefix += ele
            r = prefix % k
            if r in h:
                res += h[r]
            h[r] = h.get(r, 0) + 1
        return res

        