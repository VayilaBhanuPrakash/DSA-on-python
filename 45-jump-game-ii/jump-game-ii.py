class Solution:
    def jump(self, nums: list[int]) -> int:
        
        curr = 0
        jump = 0
        res = 0
        for i in range(len(nums) - 1):
            jump = max(jump, i + nums[i])

            if i == curr:
                res += 1
                curr = jump
        return res
            

        