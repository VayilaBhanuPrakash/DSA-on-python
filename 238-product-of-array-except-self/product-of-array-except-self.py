class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        start = [0] * n
        start[0] = nums[0]
        for i in range(1,n):
            start[i] = start[i - 1] * nums[i]

        end = [0] * n
        end[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            end[i] = nums[i] * end[i + 1]
        
        res = [0] * n

        res[0] = end[1]
        res[n - 1] = start[n - 2]
        for i in range(1, n - 1):
            res[i] = start[i - 1] * end[i + 1]
        
        return res


        
        

        