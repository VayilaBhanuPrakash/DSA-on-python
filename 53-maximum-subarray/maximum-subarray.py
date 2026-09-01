class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        psum=0
        submax=nums[0]
        for ele in nums:
            psum=max(psum+ele,ele)
            submax=max(psum,submax)
        return submax
        