class Solution:
    def minMoves(self, nums: list[int]) -> int:
        x = min(nums)
        summ = sum(nums)
        n = len(nums)
        return summ - x * n
        