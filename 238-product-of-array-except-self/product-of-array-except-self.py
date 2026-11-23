class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        prefixx = 1
        for i in range(len(nums)):
            prefix[i] = prefixx
            prefixx = prefixx * nums[i]
        print(prefix)
        
        res = [0] * len(nums)
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] = prefix[i] * suffix
            suffix *= nums[i]

        return res


        
        

        