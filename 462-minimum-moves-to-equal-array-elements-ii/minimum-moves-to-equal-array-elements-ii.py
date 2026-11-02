class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)
        middle = nums[n // 2] 
        res = 0
        for ele in nums:
            res += abs(ele - middle)
        return res
        