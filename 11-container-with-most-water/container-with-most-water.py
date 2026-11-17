class Solution:
    def maxArea(self, nums: list[int]) -> int:
        i = 0
        j = len(nums) - 1
        ans = 0
        while i < j:
            ans = max(ans, (j - i) * min(nums[i],nums[j]))
            if nums[i] < nums[j]:
                i += 1
            elif nums[i] > nums[j]:
                j -= 1
            else:
                i += 1
                j -= 1
        return ans

        



        
        