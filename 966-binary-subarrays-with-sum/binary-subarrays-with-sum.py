class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        def AtMost(nums, k):
            res = 0
            i = 0
            summ = 0
            for j in range(len(nums)):
                summ += nums[j]

                while summ > k:
                    summ -= nums[i]
                    i += 1
                
                res += j - i + 1
            return res
        if goal == 0:
            return AtMost(nums, goal)
        return AtMost(nums, goal) - AtMost(nums, goal - 1)


        