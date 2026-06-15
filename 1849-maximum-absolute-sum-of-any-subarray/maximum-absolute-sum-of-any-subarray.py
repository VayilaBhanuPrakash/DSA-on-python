class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        psum = float('-inf')
        positive_sum = float('-inf')
        for ele in nums:
            psum = max(psum + ele, ele)
            positive_sum = max(positive_sum, psum)

        nsum = float('inf')
        negative_sum = float('inf')
        for ele in nums:
            nsum = min(nsum + ele, ele)
            negative_sum = min(negative_sum, nsum)
        
        return max(positive_sum, -negative_sum)
        