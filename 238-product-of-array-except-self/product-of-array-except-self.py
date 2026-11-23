class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        res[0] = 1
        for i in range(1, len(nums)):
            res[i] = res[i - 1] * nums[i - 1]
        RightProd = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] = res[i] * RightProd
            RightProd *= nums[i]

        return res
        


        