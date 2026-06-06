class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        leftSum = [0 for i in range(n)]
        rightSum = [0 for i in range(n)]
        p_sum = 0
        s_sum = 0
        for i in range(n):
            leftSum[i] = p_sum
            rightSum[n-i-1] = s_sum
            p_sum += nums[i]
            s_sum += nums[n-i-1]
        res = [0 for i in range(n)]
        for i in range(n):
            if i == 0:
                res[i] = rightSum[i]
            elif i == n-1:
                res[i] =leftSum[i]
            else:
                res[i] = abs(leftSum[i] - rightSum[i])
        return res
        