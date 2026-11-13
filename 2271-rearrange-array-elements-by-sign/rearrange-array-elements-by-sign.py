class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        pos = []
        neg = []
        for ele in nums:
            if ele > 0:
                pos.append(ele)
            else:
                neg.append(ele)
        res = []
        for i in range(len(pos)):
            res.append(pos[i])
            res.append(neg[i])
        return res

        