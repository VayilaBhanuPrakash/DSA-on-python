class Solution:
    def maxArea(self, nums: list[int]) -> int:
        n = len(nums)
        leftmax = [0 for _ in range(n)]
        leftmax[0] = nums[0]
        for i in range(1,n):
            leftmax[i] = max(leftmax[i-1],nums[i])

        rightmax = [0 for _ in range(n)]
        rightmax[n-1] = nums[n-1]
        for i in range(n-1-1,-1,-1):
            rightmax[i] = max(rightmax[i+1],nums[i])
        i = 0
        j = n - 1
        res = 0
        while i < j:
            val = min(leftmax[i],rightmax[j]) * (j - i)
            res = max(val,res)
            if leftmax[i] < rightmax[j]:
                i += 1
            else:
                j -= 1
        return res
        