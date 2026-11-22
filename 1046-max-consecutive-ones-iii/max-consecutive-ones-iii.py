class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        count = 0
        n = len(nums)
        for right in range(n):
            if nums[right] == 0:
                count += 1
            if count > k:
                if nums[left] == 0:
                    count -= 1
                left += 1
        return n - left

            

