class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        if n<3:
            return -1
        return nums[n//2]

        