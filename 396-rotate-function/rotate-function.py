class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:

        n = len(nums)
        summ = sum(nums)

        total = 0
        for i in range(1,n):
            total += i * nums[i]

        ans = total

        for k in range(1,n):
            total = total + summ - n * nums[n - k]
            ans = max(ans,total)

        return ans


        