class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        res = [0] * len(nums)

        pos_index = 0
        neg_index = 1
        for ele in nums:
            if ele > 0:
                res[pos_index] = ele
                pos_index += 2
            else:
                res[neg_index] = ele
                neg_index += 2
        return res

        