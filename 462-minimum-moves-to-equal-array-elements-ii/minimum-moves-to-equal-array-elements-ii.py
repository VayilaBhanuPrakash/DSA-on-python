class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        middle = nums[len(nums) // 2]
        res = 0
        for ele in nums:
            res = res + abs(ele - middle)
        return res
        
        