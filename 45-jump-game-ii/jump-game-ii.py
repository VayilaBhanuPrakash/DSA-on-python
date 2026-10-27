class Solution:
    def jump(self, nums: list[int]) -> int:
        jump = 0
        curr_index = 0
        res = 0
        for i in range(len(nums)-1):
            jump = max(jump, i + nums[i])
            if i == curr_index:
                res += 1
                curr_index = jump
        return res
        