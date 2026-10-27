class Solution:
    def jump(self, nums: List[int]) -> int:
        jump = 0
        curr_end = 0
        max_jump = 0

        for i in range(len(nums) - 1):
            max_jump = max(max_jump, i + nums[i])

            if i == curr_end:
                jump += 1
                curr_end = max_jump
                
        return jump

        
