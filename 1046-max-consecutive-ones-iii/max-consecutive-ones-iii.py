class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i = 0
        n = len(nums)
        count = 0
        res = 0
        for j in range(n):
            if nums[j] == 0:
                count += 1
            while count > k:
                if nums[i] == 0:
                    count -= 1
                i += 1
            res = max(res,j - i + 1)
        return res

            

