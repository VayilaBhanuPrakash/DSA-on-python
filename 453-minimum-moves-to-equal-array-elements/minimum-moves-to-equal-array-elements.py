class Solution:
    def minMoves(self, nums: list[int]) -> int:
        x = min(nums)
        count = 0
        for ele in nums:
            count = count + (ele - x)
        return count
        