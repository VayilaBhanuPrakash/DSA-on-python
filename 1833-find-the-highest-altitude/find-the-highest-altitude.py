class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res=0
        summ=0
        for ele in gain:
            summ+=ele
            res=max(res,summ)
        return res
        