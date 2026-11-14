class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        psum = [0] * (len(nums) + 1) 

        for i in range(len(nums)):
            psum[i + 1] = psum[i] + nums[i]
        res = float('inf')
        flag = 0
        for i in range(len(nums) - l + 1):
            for j in range(i + l - 1, min(i + r,len(nums))):
                summ = psum[j + 1] - psum[i]
                if summ > 0:
                    flag = 1
                    res = min(res,summ)
        if flag:
            return res
        return -1
        