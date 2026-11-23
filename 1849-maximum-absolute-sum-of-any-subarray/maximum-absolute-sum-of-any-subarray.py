class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        psum = float('-inf')
        prefix = 0
        for ele in nums:
            prefix = max(prefix + ele, ele)
            psum = max(psum,prefix)
        
        nsum = float('inf')
        prefix = 0
        for ele in nums:
            prefix = min(prefix + ele, ele)
            nsum = min(nsum, prefix)
        
        return max(psum, -nsum)

        