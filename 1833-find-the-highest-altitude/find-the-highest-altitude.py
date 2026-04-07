class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        Max=0
        Sum=0
        for ele in gain:
            Sum+=ele
            Max=max(Sum,Max)
        return Max

        