class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        psum = float('-inf')
        prefix = 0
        for i in range(len(nums)):
            prefix = max(prefix + nums[i], nums[i])
            psum = max(psum,prefix)
        
        nsum = float('inf')
        prefix = 0
        for i in range(len(nums)):
            prefix = min(prefix + nums[i], nums[i])
            nsum = min(nsum, prefix)
        
        return max(psum, -nsum)

        