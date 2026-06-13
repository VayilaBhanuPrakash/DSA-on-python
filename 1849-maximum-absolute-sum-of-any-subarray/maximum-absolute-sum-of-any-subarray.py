class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        psum = float('-inf')
        pmaxsum = float('-inf')
        for ele in nums:
            psum = max(psum + ele , ele)
            pmaxsum = max(psum,pmaxsum)
                

        nsum = float('inf')
        nminsum = float('inf')
        for ele in nums:
            nsum = min(nsum + ele , ele)
            nminsum = min(nsum,nminsum)

        
        return max(pmaxsum,-nminsum)

        